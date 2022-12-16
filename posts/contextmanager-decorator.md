---
published: 2018-04-05
id: 38
author: pushtaev
---

# @contextmanager decorator

Generators are one of the most influential Python mechanics.
They have many uses, and one of them is to create context managers easily.
Usually, you have to manually define `__enter__` and `__exit__` magic methods,
but [@contextmanager decorator](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) from `contextlib` makes it far more convenient:

```python
from contextlib import contextmanager

@contextmanager
def atomic():
    print('BEGIN')

    try:
        yield
    except Exception:
        print('ROLLBACK')
    else:
        print('COMMIT')
```

Now `atomic` is a context manager that can be used like this:

```ipython
In : with atomic():
...:     print('ERROR')
...:     raise RuntimeError()
...:
BEGIN
ERROR
ROLLBACK
```

Additionally, the `@contextmanager` magic allows to use it as a decorator as well as a context manager:

```ipython
In : @atomic()
...: def ok():
...:     print('OK')
...:
In : ok()
...:
BEGIN
OK
COMMIT
```
