---
author: orsinium
published: 2023-01-03
traces:
  - [{function: isinstance}]
depends_on:
  - reveal-type
---

# isinstance

The `isinstance` function checks whether an object is an instance of a class or of a subclass thereof:

```python
class A: pass
class B(A): pass
b = B()
isinstance(b, B) # True
isinstance(b, A) # True
isinstance(b, object) # True
isinstance(b, str) # False
isinstance(str, type) # True
```

Type-checkers understand `isinstance` checks and use them to refine the type:

```python
a: object
reveal_type(a)
# ^ Revealed type is "builtins.object"
if isinstance(a, str):
    reveal_type(a)
    # ^ Revealed type is "builtins.str"
```

One more cool thing about `isinstance` is that you can pass in it a tuple of types to check if the object is an instance of any of them:

```python
isinstance(1, (str, int)) # True
```
