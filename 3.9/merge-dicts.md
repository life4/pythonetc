There are a lot of ways to merge two dicts:

1. Long but simple:

```python
merged = d1.copy()
merged.update(d2)
```

2. [Unpacking](https://t.me/pythonetc/538) (keys must be strings):

```python
merged = {**d1, **d2}
```

3. Unpacking again:

```python
merged = dict(d1, **d2)
```

4. `collections.ChainMap`. Result isn't `dict` but so.

In python 3.9, [PEP-584](https://www.python.org/dev/peps/pep-0584/) introduced the 5th way. Meet the `|` operator for `dict`!

```python
merged = d1 | d2
```

Basically, that's the same as the first way but shorter and can be inlined.
