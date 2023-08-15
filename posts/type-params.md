---
author: orsinium
published: 2023-08-17
pep: 695
python: "3.12"
topics:
  - typing
---

# Type parameter syntax

[PEP 695](https://peps.python.org/pep-0695/) (will land in Python 3.12) introduced a new, more concise, way to declare type parameters.

Before:

```python
from typing import Generic, Iterable, TypeVar

T = TypeVar('T')

def max(args: Iterable[T]) -> T:
  ...

class Queue(Generic[T]):
  def push(self, item: T) -> None:
    ...
```

After:

```python
from typing import Iterable

def max[T](args: Iterable[T]) -> T:
  ...

class Queue[T]:
  def push(self, item: T) -> None:
    ...
```

And you can also add constraints to type variables.

Before:

```python
from typing import Callable, TypeVar

C = TypeVar('C', bound=Callable)

def decorator(f: C) -> C:
  ...
```

After:

```python
from typing import Callable

def decorator[C: (Callable, )](f: C) -> C:
  ...
```

The main benefit of the new syntax is that type constraints are now scoped to the class or function that uses them. The old `TypeVar` syntax made you declare a global variable at the top of the file that might be far from the class or function declaration that needs them and is often reused in multiple places.
