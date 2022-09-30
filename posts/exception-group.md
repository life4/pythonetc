---
author: orsinium
traces:
  - [{exception: ExceptionGroup}]
pep: 654
python: "3.11"
---

# ExceptionGroup

[PEP 654](https://peps.python.org/pep-0654/) (landed in Python 3.11) introduced `ExceptionGroup`. It's an exception that nicely wraps and shows multiple exceptions:

```python
try:
  1/0
except Exception as e:
  raise ExceptionGroup('wow!', [e, ValueError('oh no')])

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# ZeroDivisionError: division by zero

# During handling of the above exception, another exception occurred:

#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 4, in <module>
#   | ExceptionGroup: wow! (2 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | Traceback (most recent call last):
#     |   File "<stdin>", line 2, in <module>
#     | ZeroDivisionError: division by zero
#     +---------------- 2 ----------------
#     | ValueError: oh no
#     +------------------------------------
```

It's very helpful in many cases when there are multiple unrelated exceptions occured and you want to show all of them: when retrying an operation or when calling multiple callbacks.
