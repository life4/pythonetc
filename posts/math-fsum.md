---
author: orsinium
traces:
  - [module: math, function: fsum]
---

# math.fsum

The `float` type is [infamous for being not as precise as you might expect](https://t.me/pythonetc/201). When you add 2 numbers, the result might contain a small error in precision. And the more numbers you add together, the higher the error:

```python
sum([.9] * 1_000)
# 899.9999999999849

sum([.9] * 1_000_000)
# 900000.0000153045
```

If you want to minimize the error when summing together a list of floats, use `math.fsum`:

```python
import math

math.fsum([.9] * 1_000_000)
# 900000.0
```
