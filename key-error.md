Most of the standard exceptions raised from the standard library or built-ins have quite descriptive self-contained message:

```python
try:
  [][0]
except IndexError as e:
  exc = e

str(exc)
# 'list index out of range'
```

However, `KeyError` is different: instead of user-friendly error message it contains the key which is missed:

```python
try:
  {}[0]
except KeyError as e:
  exc = e

# str(exc)
# '0'
```

So, if you log an exception as string, make sure you save traceback as well, or at least use `repr` instead of `str`:

```python
repr(exc)
# 'KeyError(0)'
```
