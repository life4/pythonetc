---
published: 26 August 2021, 18:00
author: orsinium
---

# Development Mode

Python 3.7 introduced [Development Mode](https://docs.python.org/3.9/library/devmode.html). The mode can be activated with the `-X dev` argument and it makes the interpreter produce some helpful warnings. For instance:

+ Unclosed files.
+ Unawaited coroutines.
+ Unknown encoding for `str.encode` (by default, it is unchecked for empty strings).
+ Memory allocation issues.

```bash
$ echo 'open("/dev/null")' > tmp.py
$ python3 -X dev tmp.py
tmp.py:1: ResourceWarning: unclosed file <_io.TextIOWrapper name='/dev/null' mode='r' encoding='UTF-8'>
  open("/dev/null")
ResourceWarning: Enable tracemalloc to get the object allocation traceback
```
