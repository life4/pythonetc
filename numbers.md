Module [numbers](https://docs.python.org/3/library/numbers.html) was introduced by [PEP-3141](https://www.python.org/dev/peps/pep-3141/) in Python 2.6. It implements the numbers hierarchy, inspired by [Scheme](https://en.wikipedia.org/wiki/Scheme_programming_language):

```python
Number :> Complex :> Real :> Rational :> Integral
```

They are [ABC](https://t.me/pythonetc/550) classes, so they can be used in `isinstance` checks:

```python
import numbers
isinstance(1, numbers.Integral)
# True

isinstance(1, numbers.Real)
# True

isinstance(1.1, numbers.Integral)
# False
```

+ `int` is `Integral`.
+ [fractions.Fraction](https://t.me/pythonetc/201) is `Rational`.
+ `float` is `Real`.
+ `complex` is `Complex` (wow!)
+ [decimal.Decimal](https://t.me/pythonetc/201) is `Number`.

In theory, `Decimal` should be `Real` but it's not because `Decimal` doesn't interoperate with `float`:

```python
Decimal(1) + 1.1
# TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
```

The most fun thing about `numbers` is that [it's not supported by mypy](https://github.com/python/mypy/issues/3186).
