---
published: 2018-05-13
id: 88
author: pushtaev
---

# ...

When you write custom `__repr__` for some object, you usually want to include representation of its attributes.
You should be careful to call `repr()` explicitly, since formatting calls `str()` instead.

Here is a simple example:

```python
class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def __repr__(self):
        class_name = type(self).__name__
        repr_left = repr(self.left)
        repr_right = repr(self.right)
        return f'{class_name}({repr_left}, {repr_right})'
```

The problem with calling `repr` on some other objects is that you can't guarantee it's not the same object and the call isn't recursive:

```ipython {continue}
In : p = Pair(1, 2)
In : p
Out: Pair(1, 2)
In : p.right = p
```

```ipython {continue} {shield:RecursionError} {merge} {python-interactive-no-check}
In : p
Out: [...]
RecursionError: maximum recursion depth exceeded while calling a Python object
```

To easily solve this problem you can use `reprlib.recursive_repr` decorator:

```python {hide} {continue}
import reprlib
```

```python {continue}
@reprlib.recursive_repr()
def __repr__(self):
    class_name = type(self).__name__
    repr_left = repr(self.left)
    repr_right = repr(self.right)
    return f'{class_name}({repr_left}, {repr_right})'
```

```python {hide} {continue}
Pair.__repr__ = __repr__
```

Now it works:

```ipython {continue}
In : p = Pair(1, 2)
In : p.right = p
In : p
Out: Pair(1, ...)
```
