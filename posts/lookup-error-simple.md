---
author: pushtaev
id: 23
published: 2018-03-24
---

# LookupError

If you want to catch both `IndexError` and `KeyError`,
you may and should use `LookupError`, their common ancestor.
It proved to be useful while accessing complex nested data:

```python {hide}
config = {}
```

```python {continue}
try:
    db_host = config['databases'][0]['hosts'][0]
except LookupError:
    db_host = 'localhost'
```
