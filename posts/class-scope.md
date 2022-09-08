---
published: 27 January 2021, 19:00
author: orsinium
---

# class scope

Today Guido van Rossum [posted a Python riddle](https://twitter.com/gvanrossum/status/1354305179244392453):

```python
x = 0
y = 0
def f():
    x = 1
    y = 1
    class C:
        print(x, y)  # What does this print?
        x = 2
f()
```

The answer is `0 1`.

The first tip is if you replace the class with a function, it will fail:

```python
x = 0
y = 0
def f():
    x = 1
    y = 1
    def f2():
        print(x, y)
        x = 2
    f2()
f()
# UnboundLocalError: local variable 'x' referenced before assignment
```

Why so? The answer can be found in the documentation (see [Execution model](https://docs.python.org/3/reference/executionmodel.html)):

> If a variable is used in a code block but not defined there, it is a free variable.

So, `x` is a free variable but `y` isn't, this is why behavior for them is different. And when you try to use a free variable, the code fails at runtime because you haven't defined it yet in the current scope but will define it later.

Let's disassemble the snippet above:

```python
import dis
dis.dis("""[insert here the previous snippet]""")
```

It outputs a lot of different things, this is the part we're interested in:

```js
  8  0 LOAD_GLOBAL    0 (print)
     2 LOAD_FAST      0 (x)
     4 LOAD_DEREF     0 (y)
     6 CALL_FUNCTION  2
     8 POP_TOP
```

Indeed, `x` and `y` have different instructions, and they're different at bytecode-compilation time. Now, what's different for a class scope?

```python
import dis
dis.dis("""[insert here the first code snippet]""")
```

This is the same dis part for the class:

```js
  8  8 LOAD_NAME         3 (print)
     10 LOAD_NAME        4 (x)
     12 LOAD_CLASSDEREF  0 (y)
     14 CALL_FUNCTION    2
     16 POP_TOP
```

So, the class scope behaves differently. `x` and `y` loaded with `LOAD_FAST` and `LOAD_DEREF` for a function and with `LOAD_NAME` and `LOAD_CLASSDEREF` for a class.

The same documentation page answers how this behavior is different:

> Class definition blocks and arguments to exec() and eval() are special in the context of name resolution. A class definition is an executable statement that may use and define names. These references follow the normal rules for name resolution with an exception that unbound local variables are looked up in the global namespace.

In other words, if a variable in the class definition is unbound, it is looked up in the `global` namespace skipping enclosing `nonlocal` scope.
