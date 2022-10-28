---
author: orsinium
---

# Annotating decorators

Tip #14: it's important to correctly and thoughtfully annotate decorators. Unannotated decorators will turn into `Any` everything they decorate, making annotations for the decorated functions invisible for mypy. And incomplete annotations aren't any better.

For example, this decorator:

```python
from typing import Callable

def dec(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Let's see how it works:

```python
@dec
def f(a: int) -> int: ...

reveal_type(f)
# note: Revealed type is "def (*Any, **Any) -> Any"
```

As we can see, mypy looses all information about the function type. What we need is the power of generics:

```python
from typing import TypeVar

C = TypeVar('C')

def dec(func: C) -> C:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Using `TypeVar` tells mypy "whatever type is passed, exactly the same type will be returned". Let's run mypy:

```text
error: "object" not callable
error: Incompatible return value type (got "Callable[[VarArg(Any), KwArg(Any)], Any]", expected "C")
note: Revealed type is "def (a: builtins.int) -> builtins.int"
```

That's better. The function type is preserved but now we have two type errors in the decorator itself. We can fix "not callable" error by binding the `TypeVar` to `Callable`. Additionally, it will make sure that only callable objects are passed in `dec`.

```python
from typing import Callable, TypeVar

C = TypeVar('C', bound=Callable)
```

The "incompatible return value type" error cannot be fixed because mypy is right. You return not what you've got, you return some other function. It doesn't matter how flexible the new function is. So, just suppress the error:

```python
return wrapper  # type: ignore[return-value]
```
