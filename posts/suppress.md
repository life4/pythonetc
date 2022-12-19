---
published: 2018-04-13
id: 53
author: pushtaev
---

# suppress

If you want to ignore some exception, you probably do something like this:

```python
try:
    lst = [1, 2, 3, 4, 5]
    print(lst[10])
except IndexError:
    pass
```

That will work (without printing anything), but `contextlib` let you do the same more expressively and semantically correct:

```python
from contextlib import suppress
with suppress(IndexError):
    lst = [1, 2, 3, 4, 5]
    lst[10]
```
