---
published: 02 March 2021, 18:00
author: orsinium
---

# nonlocal

Any enclosing variable can be shadowed in the local scope without affecting the global one:

```python
v = 'global'
def f():
  v = 'local'
  print(f'f {v=}')
f()
# f v='local'

print(f'{v=}')
# v='global'
```

And if you try to use a variable and then shadow it, the code will fail at runtime:

```python
v = 'global'
def f():
  print(v)
  v = 'local'
f()
# UnboundLocalError: local variable 'v' referenced before assignment
```

If you want to re-define the global variable instead of locally shadowing it, it can be achieved using `global` and `nonlocal` statements:

```python
v = 'global'
def f():
  global v
  v = 'local'
  print(f'f {v=}')
f()
# f v='local'
print(f'g {v=}')
# g v='local'

def f1():
  v = 'non-local'
  def f2():
    nonlocal v
    v = 'local'
    print(f'f2 {v=}')
  f2()
  print(f'f1 {v=}')
f1()
# f2 v='local'
# f1 v='local'
```

Also, `global` can be used to skip non-local definitions:

```python
v = 'global'
def f1():
    v = 'non-local'
    def f2():
        global v
        print(f'f2 {v=}')
    f2()
f1()
# f2 v='global'
```

To be said, using `global` and `nonlocal` is considered a bad practice that complicates the code testing and usage. If you want a global state, think if it can be achieved in another way. If you desperately need a global state, consider using [singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern) which is a little bit better.
