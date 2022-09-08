---
published: 2020-11-24
author: orsinium
pep: 3155
python: "3.3"
---

# `__qualname__` (PEP-3155)

In Python 3.3, [PEP-3155](https://www.python.org/dev/peps/pep-3155/) introduced a new `__qualname__` attribute for classes and functions which contains a full dotted path to the definition of the given object.

```python
class A:
  class B:
    def f(self):
      def g():
        pass
      return g

A.B.f.__name__
# 'f'

A.B.f.__qualname__
# 'A.B.f'

g = A.B().f()
g.__name__
# 'g'

g.__qualname__
# 'A.B.f.<locals>.g'
```
