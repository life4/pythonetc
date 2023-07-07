---
published: 2022-07-05
id: 686
author: orsinium
traces:
  - [module: atexit]
---

# atexit

The module [atexit](https://docs.python.org/3/library/atexit.html) allows registering hooks that will be executed when the program terminates.

There are only a few cases when it is NOT executed:

+ When `os._exit` (don't confuse with `sys.exit`) is called.
+ When the interpreter failed with a fatal error.
+ When the process is hard-killed. For example, someone executed [kill -9](https://askubuntu.com/a/184074) or the system is ran out of memory.

In all other cases, like an unhandled exception or `sys.exit`, the registered hooks will be executed.

A few use cases:

+ Finish pending jobs
+ Send pending log messages into the log system
+ Save interactive interpreter history

However, keep in mind that there is no way to handle unhandled exceptions using `atexit` because it is executed after the exception is printed and discarded.

```python
import atexit

atexit.register(print, 'FINISHED')
1/0
```

Output:

```plain
Traceback (most recent call last):
  File "example.py", line 4, in <module>
    1/0
ZeroDivisionError: division by zero
FINISHED
```
