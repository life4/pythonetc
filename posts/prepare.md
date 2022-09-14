---
published: 2020-07-09
id: 579
author: orsinium
topics:
  - dunder
qname: __prepare__
---

# `__prepare__`

Magic method `__prepare__` on metaclass is called on class creation. It must return a dict instance that then will be used as `__dict__` of the class. For example, it can be used to inject variables into the function scope:

```python
class Meta(type):
    def __prepare__(_name, _bases, **kwargs):
        d = {}
        for k, v in kwargs.items():
            d[k] = __import__(v)
        return d

class Base(metaclass=Meta):
    def __init_subclass__(cls, **kwargs):
      pass

class C(Base, m='math'):
    mypi = m.pi

C.mypi
# 3.141592653589793

C.m.pi
# 3.141592653589793
```
