---
published: 2020-08-18
id: 590
author: orsinium
qname: fnmatch
---

# fnmatch

Module [fnmatch](https://docs.python.org/3/library/fnmatch.html) provides a few functions to work with Unix-like patterns:

```python
from fnmatch import fnmatch

fnmatch('example.py', '*.py')
# True

fnmatch('example.py', '*.cpp')
# False
```

Internally, it parses the given pattern and compiles it into a regular expression. So, don't expect it to be faster than [re](https://docs.python.org/3/library/re.html#module-re). Also, if you want to match actual files in the filesystem, use [pathlib.Path.glob](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob) instead.
