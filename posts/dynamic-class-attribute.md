---
published: 2020-10-08
id: 615
author: orsinium
traces:
  - [module: types, decorator: DynamicClassAttribute]
---

# types.DynamicClassAttribute

[types.DynamicClassAttribute](https://docs.python.org/3/library/types.html#types.DynamicClassAttribute) is a decorator that allows having a `@property` that behaves differently when it's called from the class and when from the instance.

```python
from types import DynamicClassAttribute

class Meta(type):
    @property
    def hello(cls):
        return f'hello from Meta ({cls})'

class C(metaclass=Meta):
    @DynamicClassAttribute
    def hello(self):
        return f'hello from C ({self})'

C.hello
# "hello from Meta (<class '__main__.C'>)"

C().hello
# 'hello from C (<__main__.C object ...)'
```

Practically, it is used only in `enum` to provide `name` and `value` properties for instances while still allowing to have `name` and `value` class members:

```python
import enum

class E(enum.Enum):
    value = 1

E.value
# <E.value: 1>

E.value.value
# 1
```
