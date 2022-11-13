---
author: pushtaev
id: 16
published: 2018-03-21
sequence: decorator-syntax
---

# Decorator syntax

Famous Python decorator syntax (`@this_one`) is a way
to call higher-order function. Back then people had to do it manually:

```python {hide}
def atomic(x):
    assert callable(x)
```    

```python {continue}
# prior to Python 2.4
def query():
    pass
query = atomic(query)

# now
@atomic
def query():
    pass
```

Basically, the identifier after `@` is what to be called.
You also can use identifier with brackets (`@atomic(skip_errors=True)`),
that is usually used for parameterized decorators.
Something like `@decorators.db.atomic(True)` also works.
Looks like you use any kind of expression as a decorator, but that is not true.
`@` must be followed by one “dotted named” (meaning something like `decorators.atomic`)
and optionally by one pair of brackets with arguments (just like a function call).
So, no `@decorators[2]` for you. Here is a line from Python grammar:

```
decorator: '@' dotted_name [ '(' [arglist] ')' ] NEWLINE
```
