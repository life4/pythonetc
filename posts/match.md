---
published: 2020-06-26
id: 575
author: orsinium
pep: 622
python: "3.10"
traces:
  - [keyword: match]
---

# match

On this Tuesday, a team of 5 authors (including Guido van Rossum) published [PEP-622](https://www.python.org/dev/peps/pep-0622/). This is a huge draft in terms of size, complexity, and impact. It is a proposal to extend Python syntax to support structural [pattern matching](https://en.wikipedia.org/wiki/Pattern_matching). Think about it as `if` statement on steroids.

A small example using `match` as [switch statement](https://en.wikipedia.org/wiki/Switch_statement):

```python
def http_error(status: int) -> str:
  match status:
    case 400:
        return 'Bad request'
    case 401:
        return 'Unauthorized'
    case _:
        return 'Something else'
```

Impractical but reach example:

```python
def inspect(obj) -> None:
  match obj:
    case 0 | 1 | 2:   # matching 2 or more exact values
      print('small number')
    case x if x > 2:  # guards
      print('big positive number')
    case [] | [_]:    # matching sequence
      print('zero or one element sequence')
    case [x, _, *_]:  # unpacking to match rest
      print('2 or more elements sequence')
      print(f'the first element is {x}')
    case {'route': route}:  # matching dicts
      print(f'dict with ONLY `route` key which is {route}')
    # case {'route': _, **_}:  # matching rest for dicts
    #   print(f'dict with `route` key')
    case str() | bytes():  # matching types
      print('something string-like')
    # case [x := [_, *_]]:  # walrus and sub-patterns
    #   print('non-empty list inside a list')
    case _:  # default case
      print('something else')
```

For objects, the check is implemented via `__match__` magic method. For `object` it does `isinstance` check. This is why `case str()` works:

```python
class object:
  @classmethod
  def __match__(cls, obj):
    if isinstance(obj, cls):
      return obj
```

Also, it is possible to match objects' attributes:

```python {no-print}
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

obj = Point(1, 2)
match obj:
  case Point(x=0, y=0):
    print('both x and y are zero')
  case Point():
    print('it is a point')
  case _:
    print('something else')
```

Also, if a class has `__match_args__`, the given arguments can be positional in the pattern:

```python
class Point:
  __match_args__ = ('x', 'y')

  def __init__(self, x, y):
    self.x = x
    self.y = y

obj = Point(1, 2)
match obj:
  case Point(0, 0):  # here args are positional now
    print('both x and y are zero')
```

You already can try it using [patma](https://github.com/gvanrossum/patma). It is a fork of CPython with the reference implementation of the draft. It is expected to land into Python in 3.10 release.
