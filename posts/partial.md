---
published: 2018-05-01
id: 74
author: pushtaev
---

# partial

Sometimes you need to create a function from a more universal one.
For example, `int()` has a `base` parameter which we would like to freeze to have new `base2` function:

```python-interactive
>>> int("10")
10
>>> int("10", 2)
2
>>> def base2(x):
...     return int(x, 2)
...
>>> base2("10")
2
```

The `functools.partial` allows you to do the same more accurate and semantically clear:

```python {hide}
from functools import partial
```

```python {continue}
base2 = partial(int, base=2)
```

It can be helpful when you need to pass a function as an argument to another higher order function, but some arguments should be locked:

```python-interactive {continue}
>>> list(map(partial(int, base=2), ["1", "10", "100"]))
[1, 2, 4]
```

Without `partial` you do something like this:

```python-interacive
>>> list(map(lambda x: int(x, base=2), ["1", "10", "100"]))
[1, 2, 4]
```
