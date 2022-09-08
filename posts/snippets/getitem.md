---
published: 2020-08-11
author: orsinium
---

# operator.getitem

When you have a dict with a deep inheritance (like a configuration file) and path in it specified as a string, there is a fun and short way how to get a value from the dict by the given path:

```python
from functools import reduce
from operator import getitem

d = {'a': {'b': {'c': 13}}}
path = 'a.b.c'
reduce(getitem, path.split('.'), d)
# 13
```
