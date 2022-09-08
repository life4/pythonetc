---
published: 18 June 2020, 18:00
author: orsinium
pep: 614
---

# decorators (PEP-614)

[Syntax for decorators is limited](https://t.me/pythonetc/16) by getting attributes and calling objects:

```python
decos = {
  'id': lambda x: x,
}

@decos['id']
def f(): pass
# SyntaxError: invalid syntax
```

Python 3.9 (via [PEP-614](https://www.python.org/dev/peps/pep-0614/)) relaxes with restriction allowing to have any expression as a decorator:

```python
decos = {
  'id': lambda x: x,
}

@decos['id']
def f(): pass

f
# <function f at ...>
```

You can use matrix multiplication to make it confusing (don't try it at home!):

```python
class D:
  f = None
  def __init__(self, name):
    self.name = name

  def __call__(self, *args, **kwargs):
    # on the first call save the function
    if self.f is None:
      self.f = args[0]
      return self
    # on all the next calls call the function
    print(f'hello from {self.name}!')
    return self.f(*args, **kwargs)

  # matrix multiplication logic
  def __matmul__(self, other):
    return lambda f: self(other(f))

# the second `@` is actually the matrix multiplication
@D('a') @D('b')
def f(): pass

f()
# hello from a!
# hello from b!
```

You can use a simple wrapper function to have any expression in older python versions:

```python
_ = lambda x: x

@_(D('a') @ D('b'))
def f(): pass
```
