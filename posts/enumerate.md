---
published: 2018-05-07
id: 82
author: pushtaev
---

# `enumerate`

In Python, `for` lets you withdraw elements from a collection without thinking about their indexes:

```python
def find_odd(lst):
    for x in lst:
        if x % 2 == 1:
            return x

    return None
```

```python {hide} {continue}
assert find_odd([2, 4, 6]) is None
assert find_odd([2, 4, 5, 6]) == 5
```

If you do care about indexes you can iterate over `range(len(lst))`:

```python
def find_odd(lst):
    for i in range(len(lst)):
        x = lst[i]
        if x % 2 == 1:
            return i, x

    return None, None
```

```python {hide} {continue}
assert find_odd([2, 4, 6]) == (None, None)
assert find_odd([2, 4, 5, 6]) == (2, 5)
```

But perhaps the more semantically correct and expressive way to do the same it to use `enumerate`:

```python
def find_odd(lst):
    for i, x in enumerate(lst):
        if x % 2 == 1:
            return i, x

    return None, None
```

```python {hide} {continue}
assert find_odd([2, 4, 6]) == (None, None)
assert find_odd([2, 4, 5, 6]) == (2, 5)
```
