---
published: 2020-11-19
id: 633
author: orsinium
traces:
  - [{type: object}, {method: __index__}]
pep: 357
---

# `__index__` (PEP-357)

In Python 2.5, [PEP-357](https://www.python.org/dev/peps/pep-0357/) allowed any object to be passed as index or slice into `__getitem__`:

```python
class L:
  def __getitem__(self, value):
    return value

class C:
  pass

L()[C]
# <class __main__.C ...>
```

 Also, it introduced a magic method `__index__`. it was passed instead of the object in slices and used in `list` and `tuple` to convert the given object to `int`:

 ```python
class C:
  def __index__(self):
    return 1

# Python 2 and 3
L()[C()]
# <__main__.C ...>

L()[C():]
# Python 2:
# slice(1, 9223372036854775807, None)
# Python 3:
# slice(<__main__.C object ...>, None, None)

# python 2 and 3
[1,2,3][C()]
# 2
```

The main motivation to add `__index__` was to support slices in numpy with custom number types:

```python
two = numpy.int64(2)

type(two)
# numpy.int64

type(two.__index__())
# int
```

Now it is mostly useless. However, it is a good example of language changes to meet the needs of a particular third-party library.
