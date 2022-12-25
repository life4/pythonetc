---
published: 2018-04-30
id: 73
author: pushtaev
---

# Communication with subprocess

Creating an external process in Python is an easy task, you can do it with `subprocess` module.
However, reading both `stdout` and `stderr` of the spawned process may be more challenging.

Let's suppose we ask `Popen` to create two pipes, one for `stdout` and one for `stderr`:

```python {hide}
import subprocess
```

```python {continue}
p = subprocess.Popen(
    ["python", "-c", "..."],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
```

Now we have to read from them. The problem is, you can't just do `readline()` for any of those pipes since it can cause deadlocks. Consider the more concrete example:

```python {no-print}
import subprocess

SUBPROCESS_CODE = """
import sys
sys.stderr.write('err')
print('out')
"""

p = subprocess.Popen(
    ["python", "-c", SUBPROCESS_CODE],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

print(p.stdout.readline())
```

The primary process creates the child and waits for `stdout`.
The child process first writes to `stderr` pipe and then to `stdout`.
The main process successfully receives `'out'` from the pipe.
But what about `'err'`? It's stored in the pipe buffer until the main process does `p.stderr.readline()`. But what if the buffer is full?

```python {no-run}
import subprocess

SUBPROCESS_CODE = """
import sys
for _ in range(100000):
    sys.stderr.write('err')
print('out')
"""

p = subprocess.Popen(
    ["python", "-c", SUBPROCESS_CODE],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

print(p.stdout.readline())
```

In this case `sys.stderr.write('err')` will be blocked at some point until someone reads from the buffer.
But no one ever will: the main process waits for data in `stdout`.
This is the deadlock we are talking about.

To solve this problem, you should read from both `stdout` and `stderr` at once.
You can do it with `select` module or simply use `p.communicate()`.
The second approach is much more straightforward but doesn't let you read data line by line.
