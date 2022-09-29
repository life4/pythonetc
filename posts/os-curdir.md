---
author: orsinium
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

It's a constant indicating how the current directory is denoted in the current OS. And for all OSes that CPython supports (WIndows and POSIX) it's always a dot. It might be different, though, if you run your code with MicroPython on some niche OS.

Anyway, to actualy get the path to the current directory, you need `os.getcwd`:

```python
os.getcwd()
# '/home/gram'
```

Or use pathlib:

```python
from pathlib import Path
Path().absolute()
# PosixPath('/home/gram')
```
