---
published: 2018-04-19
id: 60
author: pushtaev
---

# attrs

A lot of Python classes start with a similar boilerplate: straightforward constructor, trivial `repr` and stuff like that:

```python
class Server:
    def __init__(self, ip, version=4):
        self.ip = ip
        self._version = version

    def __repr__(self):
        return '{klass}("{ip}", {version})'.format(
            klass=type(self).__name__,
            ip=self.ip,
            version=self._version,
        )
```

One way to deal with it is to use popular [attrs](https://github.com/python-attrs/attrs) package, which does a lot of default things automatically driving by few declarations:

```python {hide}
import attr
```

```python {continue}
@attr.s
class Server:
    ip = attr.ib()
    _version = attr.ib(default=4)

server = Server(ip='192.168.0.0.1', version=4)
```

It not only creates initializer and `repr` for you but a complete set of comparison methods as well.

That said, there is the [upcoming change](https://www.python.org/dev/peps/pep-0557/) in Python 3.7, that brings us *data classes*, the standard library addition that should solve the same problem (and more). It uses the [variable annotations](https://www.python.org/dev/peps/pep-0526/), another comparably new Python feature. Here is an example:

```python {hide}
from dataclasses import dataclass
```

```python {continue}
@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```
