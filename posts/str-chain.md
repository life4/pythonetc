---
published: 2021-05-06
author: orsinium
qname: str.__getitem__
---

# `str.__getitem__` quirks

Since Python doesn't have a `char` type, an element of `str` is always `str`:

```python
'@pythonetc'[0][0][0][0][0]
# '@'
```

This is an infinite type and you can't construct in a strictly typed language (and why would you?) because it's unclear how to construct the first instance ([thing-in-itself](https://en.wikipedia.org/wiki/Thing-in-itself)?). For example, in Haskell:

```haskell
Prelude> str = str str

<interactive>:1:7: error:
    • Occurs check: cannot construct the infinite type: t1 ~ t -> t1
```
