---
author: VadimPushtaev
id: 13
published: 2018-03-19
sequence: dict-keys
---

# dict VS OrderedDict

If `dict` remembers the order of elements in Python3.6+, why do you need `collections.OrderedDict` anymore? That's why:

```python {hide}
from collections import OrderedDict
```

```python-interactive {continue}
>>> OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1)
False
>>> dict(a=1, b=2) == dict(b=2, a=1)
True
```
