# faulthandler

The module [faulthandler](https://docs.python.org/3/library/faulthandler.html) allows to register a handler that will dump the current stack trace in a specific file (stderr by default) upon receiving a specific signal.

Dump stack trace every second:

```python
import faulthandler
from time import sleep

faulthandler.dump_traceback_later(
  timeout=2,
  repeat=True,
)
for i in range(5):
  print(f"iteration {i}")
  sleep(1)
```

Output:

```plain
iteration 0
iteration 1
Timeout (0:00:02)!
Thread 0x00007f8289147740 (most recent call first):
  File "tmp.py", line 10 in <module>
iteration 2
iteration 3
Timeout (0:00:02)!
Thread 0x00007f8289147740 (most recent call first):
  File "tmp.py", line 10 in <module>
iteration 4
```
