---
published: 2018-05-16
id: 91
author: pushtaev
---

# Source file path

Python lets you know the path to any source file. Within that file, `__file__` returns the *relative* path to it:

```bash
$ cat test/foo.py
print(__file__)
$ python test/foo.py
test/foo.py
```

The typical usage for that is to find the path where the script is located. It can be helpful for finding other files such as configs, assets, etc.

To get the absolute path form the relative one you can use `os.path.abspath`. So the common idiom to get the script directory path is:

```python {hide}
import os
__file__ = ''
```

```python {continue}
dir_path = os.path.dirname(os.path.abspath(__file__))
```
