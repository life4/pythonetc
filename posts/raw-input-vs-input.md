---
published: 2018-05-11
id: 86
author: pushtaev
---

# raw_input vs input

To read a line from `stdin` before Python 3, you had to use the `raw_input` function instead of `input`.
Usage of `input` was pretty dangerous since it *executes* the input line:

```bash
$ echo '[x ** 2 for x in range(10)]' | python2 -c 'print input()'
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

In Python 3 `input` just reads the line and `raw_input` is gone.

If you want to support both Python 2 and Python 3, you can do something like this:

```python
from contextlib import suppress

with suppress(NameError):
    input = raw_input
```

The popular `six` module already does this for you. It provides `input` function that only reads the line.
