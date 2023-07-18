---
published: 2018-05-17
id: 92
author: pushtaev
---

# tempfile

Unit-tests you write may require some temporary files or directories. The `tempfile` module can help you to achieve that.

Since temporary stuff usually should be removed after use, `tempfile` provides context manager as well as plain functions:

```python {hide}
import tempfile
import os

def files_of(dir_path):
    return set(os.listdir(dir_path))
```

```python {continue}
with tempfile.TemporaryDirectory() as dir_path:
    open(os.path.join(dir_path, 'a'), 'w').close()
    open(os.path.join(dir_path, 'b'), 'w').close()
    open(os.path.join(dir_path, 'c'), 'w').close()

    assert files_of(dir_path) == {'a', 'b', 'c'}
```
