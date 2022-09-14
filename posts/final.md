---
published: 2020-08-06
id: 587
author: orsinium
pep: 591
python: "3.8"
topics:
  - stdlib
  - decorator
  - typing
qname: typing.final
---

# typing.final

Some languages, like Java, allow you to mark a class as `final` that means you can't inherit from it. There is how it can be implemented in a few lines (thanks to [Nikita Sobolev](https://github.com/sobolevn) for the implementation!):

```python
def _init_subclass(cls, *args, **kwargs) -> None:
    raise TypeError('no subclassing!')

def final(cls):
    setattr(cls, '__init_subclass__', classmethod(_init_subclass))
    return cls

@final
class A:
    pass

class B(A):
    pass
# TypeError: no subclassing!
```

In python 3.8, [PEP-591](https://www.python.org/dev/peps/pep-0591/) introduced [typing.final](https://docs.python.org/3/library/typing.html#typing.final). It doesn't make a runtime check but is processed by mypy at static type checking instead.
