---
author: orsinium
topics:
  - typing
traces:
  - [module: typing, type: ParamSpec]
pep: 612
python: "3.10"
---

# typing.ParamSpec

Let's say, you have a typical decorator that returns a new function. Something like this:

```python {no-print}
def debug(f):
  name = f.__name__
  def inner(*args, **kwargs):
    print(f'called {name} with {args=} and {kwargs=}')
    return f(*args, **kwargs)
  return inner

@debug
def concat(a: str, b: str) -> str:
  return a + b

concat('hello ', 'world')
# called concat with args=('hello ', 'world') and kwargs={}
```

If you check the type of `concat` using [reveal_type](https://t.me/pythonetc/712), you'll see that its type is unknown because of the decorator:

```python {continue}
reveal_type(concat)
# Revealed type is "Any"
```

So, we need to properly annotate the decorator. But how?

This is not precise enough (type errors like `x: int = concat(1, 2)` won't be detected):

```python
from typing import Callable
def debug(f: Callable) -> Callable: ...
```

This is slightly better but function arguments are still untyped:

```python {continue}
from typing import TypeVar

T = TypeVar('T')
def debug(f: Callable[..., T]) -> Callable[..., T]: ...
```

This is type safe but it requres the decorated function to accept exactly 2 arguments:

```python {continue}
A = TypeVar('A')
B = TypeVar('B')
R = TypeVar('R')
def debug(f: Callable[[A, B], R]) -> Callable[[A, B], R]: ...
```

This is type safe and works on any function but it will report type error because `inner` is not guaranteed to have the same type as the passed callable (for example, someone might pass a class that is callable but we return a function):

```python {continue}
F = TypeVar('F', bound=Callable)
def debug(f: F) -> F: ...
```

[PEP 612](https://peps.python.org/pep-0612/) (landed in Python 3.10) introduced [typing.ParamSpec](https://docs.python.org/3/library/typing.html#typing.ParamSpec) which solves exactly this problem. You can use it to tell type checkers that the decorator returns a new function that accepts exactly the same arguments as the wrapped one:

```python
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

def debug(f: Callable[P, R]) -> Callable[P, R]:
  def inner(*args: P.args, **kwargs: P.kwargs) -> R:
    ...
    return f(*args, **kwargs)
  return inner

@debug
def concat(a: str, b: str) -> str:
  ...

reveal_type(concat)
# Revealed type is "def (a: str, b: str) -> str"
```
