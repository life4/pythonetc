---
published: 16 March 2021, 18:00
author: orsinium
qname: is
python: "3.8"
---

# warning about is

Starting Python 3.8, the interpreter warns about `is` comparison of literals.

Python 3.7:

```python
>>> 0 is 0
True
```

Python 3.8:

```python
>>> 0 is 0
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
```

The reason is that it is an infamous Python gotcha. While `==` does values comparison (which is implemented by calling `__eq__` magic method, in a nutshell), `is` compares memory addresses of objects. It's true for ints from -5 to 256 but it won't work for ints out of this range or for objects of other types:

```python
a = -5
a is -5   # True
a = -6
a is -6   # False
a = 256
a is 256  # True
a = 257
a is 257  # False
```
