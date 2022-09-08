---
published: 2022-09-13
author: orsinium
qname: warnings
---

# warnings

The module [warnings](https://docs.python.org/3/library/warnings.html) allows to print, you've guessed it, warnings. Most often, it is used to warn users of a library that the module, function, or argument they use is deprecated.

```python
import warnings

def g():
  return 2

def f():
  warnings.warn(
    "f is deprecated, use g instead",
    DeprecationWarning,
  )
  return g()

f()
```

The output:

```python
example.py:7: DeprecationWarning:
function f is deprecated, use g instead
  warnings.warn(
```

Note that `DeprecationWarning`, as well as [other warning categories](https://docs.python.org/3/library/warnings.html#warning-categories), is built-in and doesn't need to be imported from anywhere.

When running tests, pytest will collect all warnings and report them at the end. If you want to get the full traceback to the warning or enter there with a debugger, the easiest way to do so is to turn all warnings into exceptions:

```python
warnings.filterwarnings("error")
```

On the production, you can suppress warnings. Or, better, turn them into proper log records, so they will be collected wherever you collect logs:

```python
import logging
logging.captureWarnings(True)
```
