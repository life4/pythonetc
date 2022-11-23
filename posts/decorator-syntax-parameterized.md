---
author: pushtaev
id: 17
published: 2018-03-21
sequence: decorator-syntax
buttons:
- title: Try this code live
  url: "https://replit.com/@VadimPushtaev/unparameterizeddecorator"
---

# Parameterized decorators

Even if you use identifier with brackets as a decorator (`@atomic()`),
it  will be called again with a function as an argument:
`query = atomic(skip_errors=True)(query)`.
There are tons of examples out there on how to create parameterized decorators,
let's just move on and write a decorator that has no parameters,
but can be called with empty brackets `()`.

```python {hide}
import functools
```

```python {continue}
def atomic(func=None):
    if func is None:
        return atomic
    @functools.wraps(func)
    def wrapped():
        print('BEGIN')
        func()
        print('COMMIT')

    return wrapped

@atomic()
def query():
    print('q')
```

You can even extract that logic by decorating a decorator:

```python {hide}
import functools
```

```python {continue}
def unparameterized_decorator(decorator):
    @functools.wraps(decorator)
    def wrapped(func=None):
        if func is None:
            return decorator
        return decorator(func)

    return wrapped

@unparameterized_decorator
def atomic(func):
    @functools.wraps(func)
    def wrapped():
        print('BEGIN')
        func()
        print('COMMIT')

    return wrapped

@atomic()
def query():
    print('q')
```
