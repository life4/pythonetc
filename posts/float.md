---
published: 2021-03-18
author: orsinium
qname: float
---

# float (IEEE 754)

[Floating point numbers](https://en.wikipedia.org/wiki/Floating-point_arithmetic) in Python and most of the modern languages are implemented according to [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754). The most interesting and hardcore part is "arithmetic formats" which defines a few special values:

+ `inf` and `-inf` representing infinity.
+ `nan` representing a special "Not a Number" value.
+ `-0.0` representing "negative zero"

Negative zero is the easiest case, for all operations it considered to be the same as the positive zero:

```python
-.0 == .0  # True
-.0 < .0   # False
```

Nan returns False for all comparison operations (except `!=`) including comparison with inf:

```python
import math

math.nan < 10        # False
math.nan > 10        # False
math.nan < math.inf  # False
math.nan > math.inf  # False
math.nan == math.nan # False
math.nan != 10       # True
```

And all binary operations on nan return nan:

```python
math.nan + 10  # nan
1 / math.nan   # nan
```

You can read more about nan in previous posts:

+ <https://t.me/pythonetc/561>
+ <https://t.me/pythonetc/597>

Infinity is bigger than anything else (except nan). However, unlike in pure math, infinity is equal to infinity:

```python
10 < math.inf         # True
math.inf == math.inf  # True
```

The sum of positive and negative infinity is nan:

```python
-math.inf + math.inf  # nan
```
