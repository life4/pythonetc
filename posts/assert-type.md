---
author: orsinium
traces:
  - [module: typing, function: assert_type]
python: "3.11"
---

# typing.assert_type

The `typing.assert_type` function does nothing in runtime as most of the stuff from the `typing` module. However, if the type of the first argument doesn't match the type provided as the second argument, the type checker will return an error. It can be useful to write simple "tests" for your library to ensure it is well annotated.

For example, you have a library that defines a lot of decorators, like this:

```python
from typing import Callable, TypeVar

C = TypeVar('C', bound=Callable)

def good_dec(f: C) -> C:
    return f

def bad_dec(f) -> Callable:
    return f
```

We want to be 100% sure that all decorators preserve the original type of decorated function. So, let's write a test for it:

```python
from typing import Callable, assert_type

@good_dec
def f1(a: int) -> str: ...

@bad_dec
def f2(a: int) -> str: ...

assert_type(f1, Callable[[int], str])  # ok
assert_type(f2, Callable[[int], str])  # not ok
```
