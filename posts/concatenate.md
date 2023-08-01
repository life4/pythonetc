---
author: orsinium
published: 2023-08-10
topics:
  - typing
traces:
  - [module: typing, type: Concatenate]
depends_on:
  - param-spec
pep: 612
python: "3.10"
---

# typing.Concatenate

In addition to [typing.ParamSpec](https://docs.python.org/3/library/typing.html#typing.ParamSpec), [PEP 612](https://peps.python.org/pep-0612/) introduced [typing.Concatenate](https://docs.python.org/3/library/typing.html#typing.Concatenate) that allows describing decorators that accept fewer or more arguments that the wrapped function:

```python
from typing import Callable, Concatenate, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

class User: ...
class Request: ...
class Response: ...

def with_user(
  f: Callable[Concatenate[User, P], R],
) -> Callable[P, R]:
  def inner(*args: P.args, **kwargs: P.kwargs) -> R:
    user = User()
    return f(user, *args, **kwargs)
  return inner

@with_user
def handle_request(
  user: User,
  request: Request,
) -> Response:
  ...

request = Request()
response = handle_request(request)
```
