---
published: 2018-05-03
id: 77
author: pushtaev
---

# Is it a function?

Sometimes you want to know whether something is a function or not.
The obvious solution is to check the object class with `isinstance`.
The class of functions is `function`, but you can't access it directly.
You can instead get `type` of any existing function:

```python
FunctionType = type(lambda: None)
```

Now you can do checking:

```python {continue}
def isfunction(object):
    return isinstance(object, FunctionType)
```

Luckily all above code is already written for you: `FunctionType` is an existing member of `types` and `isfunction` already exists in the `inspect` module.

Note, that you usually don't care whether something is a function, but rather if it's callable or not. It can be done with `callable`:

```python-interacive
>>> callable(int)
True
>>> callable(42)
False
>>> callable(callable)
True
```
