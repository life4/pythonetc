An interesting story is behind [types](https://docs.python.org/3/library/types.html) module. Until Python 2.7, it had types like `IntType`, `TupleType`, `UnicodeType`, and so on. The motivation behind is that before Python 2.4 built-in functions like `int` and `str` were constructors for the types but not the types itself. Hence they couldn't be used in type checks:

```python
# before 2.4:
isinstance(1, int)
# False

import types
isinstance(1, types.IntType)

# Python 2.4 and later:
isinstance(1, int)
# True
```

The interesting thing is that the same story with [typing](https://docs.python.org/3/library/typing.html) module. Before Python 3.9 we had `typing.Dict` but now we don't need it because the `dict` type itself can be used in the same way in type annotations.
