---
published: 2020-09-01
id: 597
author: orsinium
topics:
  - stdlib
  - constant
qname: math.nan
---

# nan

Python has [NaN](https://t.me/pythonetc/561) float value and it's a rule-breaking thing:

```python
import math

sorted([5.0, math.nan, 10.0, 0.0])
# [5.0, nan, 0.0, 10.0]

3 < math.nan
# False
3 > math.nan
# False

min(3, math.nan)
# 3
min(math.nan, 3)
# nan
```

Be careful. Use `math.isnan` to check if a value is NaN.
