---
published: 2018-04-09
id: 48
author: pushtaev
---

# Generator.throw

Usually, you communicate with a generator by asking for data with `next(gen)`. You also can send some values back with `g.send(x)` in Python 3. But the technique you probably don't use every day, or maybe even isn't aware of, is throwing exceptions *inside* a generator.

With `gen.throw(e)` you may raise an exception at the point where the `gen` generator is paused, i.e. at the point of some `yield`. If `gen` catches the exception, `get.throw(e)` returns the next value yielded (or `StopIteration` is raised). If `gen` doesn't catch the exception, it propagates back to you.

```ipython {shield:RuntimeError}
In : def gen():
...:     try:
...:         yield 1
...:     except ValueError:
...:         yield 2
...:
In : g = gen()
...: 

In : next(g)
Out: 1

In : g.throw(ValueError)
Out: 2

In : g.throw(RuntimeError('TEST'))
...
RuntimeError: TEST
```

You can use it to control generator behavior more precisely, not only be sending data to it but by notifying about some problems with values yielded for example. But this is rarely required, and you have a little chance to encounter `g.throw` in the wild.

However, `@contextmanager` decorator from `contextlib` does [exactly this](https://github.com/python/cpython/blob/3.6/Lib/contextlib.py#L99) to let the code inside the context catch exceptions.

```ipython {no-print}
In : from contextlib import contextmanager
...: 
...: @contextmanager
...: def atomic():
...:     print('BEGIN')
...:     try:
...:         yield
...:     except Exception:
...:         print('ROLLBACK')
...:     else:
...:         print('COMMIT')
...: 

In : with atomic():
...:     print('ERROR')
...:     raise RuntimeError()
...: 
BEGIN
ERROR
ROLLBACK
```
