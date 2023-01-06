---
published: 2018-05-12
id: 87
author: pushtaev
---

# Function composition

Applying a function to the result of another function is called *function composition*.
If you have `f : X → Y` and `g : Y → Z`, you can create the composition function `h: X → Z`: `h(x) = g(f(x))`.

This is also denoted as `h = g ∘ f`.

In python, there is no `∘` operator, but you still can create composition functions via bare lambdas:

```ipython
In : from math import sqrt
In : sqrt_abs = lambda x: sqrt(abs(x))
In : sqrt_abs(-4)
Out: 2.0
```

To make it more semantically precise, you can create your own `compose` function. Adding clear `repr` is also a good idea. Here is an example:

```python
class compose:
    def __init__(self, *functions):
        self._functions = functions

    def __call__(self, *args, **kwargs):
        result = None
        for f in reversed(self._functions):
            result = f(*args, **kwargs)
            args = [result]
            kwargs = dict()
        return result

    def __repr__(self):
        return '{}({})'.format(
            type(self),
            ', '.join(repr(f) for f in self._functions)
        )
```

```python {hide} {continue}
a = lambda x: x + 1
b = lambda x: x * 2
assert 21 == compose(a, b)(10)
```
