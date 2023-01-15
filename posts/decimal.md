---
published: 2018-05-20
id: 95
author: pushtaev
---

# Decimal

Native Python float values use your computer hardware directly, so any value is represented internally as a binary fraction.

That means that you usually work with approximations, not exact values:

```ipython
In : format(0.1, '.17f')
Out: '0.10000000000000001'
```

The `decimal` module lets you use decimal floating point arithmetic with arbitrary precision:

```python {hide}
from decimal import Decimal
```

```ipython {continue}
In : Decimal(1) / Decimal(3)
Out: Decimal('0.3333333333333333333333333333')
```

That's still can be not enough:

```python {continue}
In : Decimal(1) / Decimal(3) * Decimal(3) == Decimal(1)
Out: False
```

For perfect computations, you can use `fractions`, that stores any number as a rational one:

```python {hide}
from fractions import Fraction
```

```python {continue}
In : Fraction(1) / Fraction(3) * Fraction(3) == Fraction(1)
Out: True
```

The obvious limitation is you still have to use approximations to irrational numbers (such as π).
