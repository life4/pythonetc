---
published: 2021-03-23
id: 655
author: orsinium
traces:
  - [type: float]
---

# float division

Infinity has an interesting behavior on division operations. Some of them are expected, some of them are surprising. Without further talking, there is a table:

```python
truediv (/)
     |   -8 |    8 | -inf |  inf
  -8 |  1.0 | -1.0 |  0.0 | -0.0
   8 | -1.0 |  1.0 | -0.0 |  0.0
-inf |  inf | -inf |  nan |  nan
 inf | -inf |  inf |  nan |  nan

floordiv (//)
     |   -8 |    8 | -inf |  inf
  -8 |    1 |   -1 |  0.0 | -1.0
   8 |   -1 |    1 | -1.0 |  0.0
-inf |  nan |  nan |  nan |  nan
 inf |  nan |  nan |  nan |  nan

mod (%)
     |   -8 |    8 | -inf |  inf
  -8 |    0 |    0 | -8.0 |  inf
   8 |    0 |    0 | -inf |  8.0
-inf |  nan |  nan |  nan |  nan
 inf |  nan |  nan |  nan |  nan
```

The code used to generate the table:

```python
import operator
cases = (-8, 8, float('-inf'), float('inf'))
ops = (operator.truediv, operator.floordiv, operator.mod)
for op in ops:
  print(op.__name__)
  row = ['{:4}'.format(x) for x in cases]
  print(' ' * 6, ' | '.join(row))
  for x in cases:
    row = ['{:4}'.format(x)]
    for y in cases:
      row.append('{:4}'.format(op(x, y)))
    print(' | '.join(row))
```
