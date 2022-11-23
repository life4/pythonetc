---
published: 2018-03-27
id: 27
author: pushtaev
sequence: abc-abstractmethod
buttons:
- title: NotImplemented docs
  url: "https://docs.python.org/3/library/constants.html#NotImplemented"
---

# NotImplemented

Remember that `NotImplemented` is not the same that `NotImplementedError`.
It's not even an exception. It's a special value (like `True` and `False`)
that has an absolutely different meaning.
It should be returned by the binary special methods
(e.g. `__eq__()`, `__add__()` etc.)
so Python tries to reflect operation.
If `a.__add__(b)` returns `NotImplemented`, Python tries to call `b.__radd__`.
