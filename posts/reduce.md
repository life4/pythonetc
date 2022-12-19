---
published: 2018-04-11
id: 50
author: pushtaev
---

# Reduce

*Reduce* is a higher-order function that processes an iterable recursively, applying some operation to the next element of the iterable and the already calculated value. You also may know it termed *fold*, *inject*, *accumulate* or somehow else.

Reduce with `result = result + element` brings you the sum of all elements, `result = min(result, element)` gives you the minimum and `result = element` works for getting the last element of a sequence.

Python provides `reduce` function (that was moved to `functools.reduce` in Python 3):

```python {hide}
from functools import reduce
```

```ipython {continue}
In : reduce(lambda s, i: s + i, range(10))
Out: 45
In : reduce(lambda s, i: min(s, i), range(10))
Out: 0
In : reduce(lambda s, i: i, range(10))
Out: 9
```

Also, if you ever need such simple lambdas like `a, b: a + b`, Python got you covered with `operator` module:

```ipython {continue}
In : from operator import add
In : reduce(add, range(10))
Out: 45
```
