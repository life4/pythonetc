---
published: 2021-04-15
id: 661
author: orsinium
qname: KeyError
---

# KeyError

Most of the exceptions raised from the standard library or built-ins have a quite descriptive self-contained message:

```python
try:
  [][0]
except IndexError as e:
  exc = e

exc.args
# ('list index out of range',)
```

However, `KeyError` is different: instead of a user-friendly error message it contains the key which is missed:

```python
try:
  {}[0]
except KeyError as e:
  exc = e

exc.args
# (0,)
```

So, if you log an exception as a string, make sure you save the class name (and the traceback) as well, or at least use `repr` instead of `str`:

```python
repr(exc)
# 'KeyError(0)'
```
