---
author: pushtaev
id: 13
published: 2018-03-19
chain:
    name: dict-keys
    idx: 1
    prev: 12
    next: null
    length: 2
    delay_allowed: true
---

# dict VS OrderedDict

If `dict` remembers the order of elements in Python3.6+, why do you need `collections.OrderedDict` anymore? That's why:

```python {skip}
from collections import OrderedDict
```

```python-interactive {continue}
>>> OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1)
False
>>> dict(a=1, b=2) == dict(b=2, a=1)
True
```
