---
author: orsinium
published: 2022-11-22
traces:
  - [{module: contextlib}, {function: chdir}]
python: "3.11"
depends_on:
  - os-curdir
---

# contextlib.chdir

I often find myself writing a context manager to temporarily change the current working directory:

```python
import os
from contexlib import contextmanager

@contextmanager
def enter_dir(path):
  old_path = os.getcwd()
  os.chdir(path)
  try:
    yield
  finally:
    os.chdir(old_path)
```

Since Python 3.11, a context manager with the same behavior is available as `contextlib.chdir`:

```python
import os
from contextlib import chdir

print('before:', os.getcwd())
# before: /home/gram
with chdir('/'):
  print('inside:', os.getcwd())
  # inside: /
print('after:', os.getcwd())
# after: /home/gram
```
