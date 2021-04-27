# types.MappingProxyType

Published: 29 April 2021, 18:00

If any function can modify any passed argument, how to prevent a value from modification? Make it immutable! That means the object doesn't have methods to modify it in place, only methods returning a new value. This is how numbers and `str` are immutable. While `list` has `append` method that modifies the object in place, `str` just doesn't have anything like this, all modifications return a new `str`:

```python
a = b = 'ab'
a is b  # True
b += 'cd'
a is b  # False
```

This is why every built-in collection has an immutable version:

+ Immutable `list` is `tuple`.
+ Immutable `set` is `frozenset`.
+ Immutable `bytearray` is `bytes`.
+ `dict` doesn't have an immutable version but since Python 3.3 it has `types.MappingProxyType` wrapper that makes it immutable:

```python
from types import MappingProxyType

orig = {1: 2}
immut = MappingProxyType(orig)

immut[3] = 4
# TypeError: 'mappingproxy' object does not support item assignment
```

And since it is just a proxy, not a new type, it reflects all the changes in the original mapping:

```python
orig[3] = 4
immut[3]
# 4
```
