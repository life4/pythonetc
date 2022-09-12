---
published: 2020-09-17
id: 606
author: orsinium
topic: stdlib
qname: sys.modules
---

# sys.modules

Python caches every imported module is `sys.modules`:

```python
import sys
import typing

sys.modules['typing']
# <module 'typing' from '/usr/local/lib/python3.7/typing.py'>

len(sys.modules)
# 637
```

You can reload any module with `importlib.reload` to force it to be executed again. Be careful, though, since every object from the module will be recreated, you can break all `isinstance` checks and have hard times with debugging it.

```python
old_list = typing.List
old_list is typing.List
# True

importlib.reload(typing)
old_list is typing.List
# False
```
