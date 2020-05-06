You can implement [f-strings](https://www.python.org/dev/peps/pep-0498/) in older Python versions by accessing [globals and locals](https://t.me/pythonetc/121) from the caller function. It is possible through getting the parent frame from the call stack:

```python
import inspect
from collections import ChainMap
def f(s):
    frame = inspect.stack()[1][0]
    vrs = ChainMap(frame.f_locals, frame.f_globals)
    return s.format(**vrs)

name = '@pythonetc'
f('Hello, {name}')
# 'Hello, @pythonetc'
```

[ChainMap](https://t.me/pythonetc/225) merges `locals` and `globals` into one mapping without need to create a new `dict`.

This implementation is a bit more limited, though. While the original f-strings can have any expression inside, our implementation can't:

```python
f'{2-1}'
# '1'
f('{2-1}')
# KeyError: '2-1'
```
