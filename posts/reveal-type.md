---
author: orsinium
topics:
  - typing
traces:
  - [{module: typing_extensions}, {function: reveal_type}]
---

# reveal_type

The `reveal_type` function doesn't exist. However, if you call it and then run a type-checker (like [mypy](https://mypy.readthedocs.io/) or pyright) on the file, it will show the type of the passed object:

```python
a = 1
reveal_type(a)
reveal_type(len)
```

Now, let's run mypy:

```bash
$ mypy tmp.py
tmp.py:2: note: Revealed type is "builtins.int"
tmp.py:3: note: Revealed type is "def (typing.Sized) -> builtins.int"
```

It's quite helpful to see what type mypy inferred for the variable in some tricky cases.

What's interesting, `typing_extensions`, for some reason, does define the `reveal_type` function at runtime:

```python
from typing_extensions import reveal_type
a = 1
reveal_type(a)
# prints: Runtime type is 'int'
reveal_type(len)
# prints: Runtime type is 'builtin_function_or_method'
```

And for curious, here is the definition:

```python
def reveal_type(__obj: T) -> T:
    print(
        f"Runtime type is {type(__obj).__name__!r}",
        file=sys.stderr,
    )
    return __obj
```
