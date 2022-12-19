---
published: 2018-04-12
id: 51
author: pushtaev
---

# functools.wraps

When you write a decorator, you almost always should use `@functools.wraps`:

```python {hide}
import functools
```

```python {continue}
def atomic(func):
    @functools.wraps(func)
    def wrapper():
        print('BEGIN')
        func()
        print('COMMIT')

    return wrapper
```

It updates `wrapper`, so it looks like an original `func`. It copies `__name__`, `__module__` and `__doc__` from `func` to `wrapper`.

It may help if you generate documentation by `pydoc`, practice `doctest` or use some introspection tools. Mind, however, that you still see the original name of the function in a stack trace (it's stored in `wrapper.__code__.co_name`).
