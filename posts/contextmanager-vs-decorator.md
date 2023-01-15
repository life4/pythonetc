---
published: 2018-05-18
id: 93
author: pushtaev
---

# Context manager vs decorator

Content managers and function decorators are pretty similar and usually interchangeable. Any context manager can be used as a function decorator as long as it's derived from `contextlib.ContextDecorator`. (Mind, that the `@contextlib.contextmanager` decorator inherits from that class automatically.)

On the other hand, you can't use any decorator as a context manager due to severe limitation: a context manager always runs a code block exactly once while a decorated function may call original one as many times as it wants (zero included).

[PEP 377](https://www.python.org/dev/peps/pep-0377/) proposed the change that allows `__enter__` to ask Python not to run a code block at all, but it was rejected.

As a workaround, you should extract a function and apply a decorator to it:

```python {hide}
from contextlib import suppress
import requests
from requests.exceptions import HTTPError
```

```python {continue}
def retry(attempts, exceptions=(Exception,)):
    def decorator(func):
        def decorated(*args, **kwargs):
            for _ in range(attempts - 1):
                with suppress(*exceptions):
                    return func(*args, **kwargs)
            return func(*args, **kwargs)  # last try
        return decorated
    return decorator

@retry(10, HTTPError)
def get(url):
    requests.get(url).raise_for_status()
```
