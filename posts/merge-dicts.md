---
published: 2020-06-04
id: 568
author: orsinium
traces:
  - [{module: dict}, {function: __or__}]
pep: 584
python: "3.9"
---

# `dict.__or__` (PEP-584)

There are a lot of ways to merge two dicts:

1. Long but simple:

    ```python
    merged = d1.copy()
    merged.update(d2)
    ```

1. [Unpacking](https://t.me/pythonetc/538):

    ```python
    merged = {**d1, **d2}
    ```

1. Unpacking again (keys must be strings):

    ```python
    merged = dict(d1, **d2)
    ```

1. `collections.ChainMap`. Result is not `dict` but so.

In python 3.9, [PEP-584](https://www.python.org/dev/peps/pep-0584/) introduced the 5th way. Meet the `|` operator for `dict`!

```python
merged = d1 | d2
```

Basically, that is the same as the first way but shorter and can be inlined.
