---
published: 2022-09-27.
author: orsinium
---

# Chain `is`

A long time ago, we already covered the chaining of comparison operations:
<https://t.me/pythonetc/411>

A quick summary is that the result of right value from each comparison gets passed into the next one:

```python
13 > 2 > 1  # same as `13 > 2 and 2 > 1`
# True

13 > 2 > 3  # same as `13 > 2 and 2 > 3`
# False
```

What's interesting, is that `is` and `in` are also considered to be operators, and so can be also chained, which can lead to unexpected results:

```python
a = None
a is None           # True, as expected
a is None is True   # False 🤔
a is None == True   # False 🤔
a is None is None   # True  🤯
```

The best practice is to use the operator chaining only to check if the value in a range using `<` and `<=`:

```python
teenager = 13 < age < 19
```
