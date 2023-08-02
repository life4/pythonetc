---
author: orsinium
id: 711
published: 2022-12-03
traces:
  - [module: typing, type: Self]
pep: 673
python: "3.11"
---

# typing.Self

[As we covered a 3 years back](https://t.me/pythonetc/451) (gosh, the channel is old), if the result of a base class is the current class, a `TypeVar` should be used as the annotation:

```python
from typing import TypeVar

U = TypeVar('U', bound='BaseUser')

class BaseUser:
  @classmethod
  def new(cls: type[U]) -> U:
    ...

  def copy(self: U) -> U:
    ...
```

That's quite verbose, but it's how it should be done for the return type for inherited classes to be correct.

[PEP 673](https://peps.python.org/pep-0673/) (landed in Python 3.11) introduced a new type `Self` that can be used as a shortcut for exactly such cases:

```python
from typing import Self

class BaseUser:
  @classmethod
  def new(cls) -> Self:
    ...

  def copy(self) -> Self:
    ...
```
