---
published: 2020-10-01
id: 612
author: orsinium
qname: contextlib.nullcontext
python: "3.7"
---

# contextlib.nullcontext

Context manager [contextlib.nullcontext](https://docs.python.org/3/library/contextlib.html#contextlib.nullcontext) is helpful when a block of code not always should be executed in a context.

A good example is a function that works with a database. If a session is passed, the function will use it. Otherwise, it creates a new session, and does it in a context to guarantee fallback logic to be executed:

```python
from contextlib import nullcontext

def get_user(id, session=None):
    if session:
        context = nullcontext(session)
    else:
        context = create_session()
    with context as session:
        ...
```

Another example is optional [suppressing errors](https://t.me/pythonetc/53):

```python
from contextlib import suppress

def do_something(silent=False):
    if silent:
        context = suppress(FileNotFoundError)
    else:
        context = nullcontext()
    with context:
        ...
```

It was added in Python 3.7. For earlier Python versions DIY:

```python
from contextlib import contextmanager

@contextmanager
def nullcontext(value=None):
    yield value
```

Another option is to use [ExitStack](https://t.me/pythonetc/415).
