---
published: 2020-09-24
id: 609
author: orsinium
traces:
  - [module: types, type: SimpleNamespace]
---

# types.SimpleNamespace

[types.SimpleNamespace](https://docs.python.org/3/library/types.html#types.SimpleNamespace) is a way to make a `dict` with access by attributes:

```python
from types import SimpleNamespace
sn = SimpleNamespace(a=1, b=2)
sn.a
# 1

sn.c
# AttributeError: ...
```

However, values from SimpleNamespace can't be accessed by getitem anymore because "There should be only one obvious way to do it":

```python
sn['a']
# TypeError: 'types.SimpleNamespace' object is not subscriptable
```
