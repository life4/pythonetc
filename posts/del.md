---
published: 2022-08-23.
author: orsinium
---

# del

The `del` statement is used to delete things. It has a few distinct behaviors, depending on what is the specified target.

If a variable specified, it will be removed from the scope in which it is defined:

```python
a = []
del a
a
# NameError: name 'a' is not defined
```

If the target has a form `target[index]`, `target.__delitem__(index)` will be called. It is defined for built-in collections to remove items from them:

```python
a = [1, 2, 3]
del a[0]
a   # [2, 3]

d = {1: 2, 3: 4}
del d[3]
d   # {1: 2}
```

Slices are also supported:

```python
a = [1, 2, 3, 4]
del a[2:]
a   # [1, 2]
```

And the last behavior, if `target.attr` is specified, `target.__delattr__(attr)` will be called. It is defined for `object`:

```python
class A:
    b = 'default'
a = A()
a.b = 'overwritten'
a.b         # 'overwritten'
del a.b
a.b         # 'default'
del a.b     # AttributeError: 'A' object has no attribute 'b'
```
