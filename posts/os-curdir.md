---
author: orsinium
published: 2022-10-18
traces:
  - [{module: os}, {function: curdir}]
  - [{module: os}, {function: getcwd}]
---

# os.curdir

The function `os.curdir` is a trap!

```python
import os
os.curdir
# '.'
```

It's a constant indicating how the current directory is denoted in the current OS. And for all OSes that CPython supports (Windows and POSIX), it's always a dot. It might be different, though, if you run your code with MicroPython on some niche OS.

Anyway, to actually get the path to the current directory, you need `os.getcwd`:

```python
os.getcwd()
# '/home/gram'
```

Or use [pathlib](https://docs.python.org/3/library/pathlib.html):

```python
from pathlib import Path
Path().absolute()
# PosixPath('/home/gram')
```
