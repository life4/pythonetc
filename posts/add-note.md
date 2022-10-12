---
author: orsinium
published: 2022-11-01
traces:
  - [{type: BaseException}, {method: add_note}]
pep: 678
python: "3.11"
---

# BaseException.add_note

[PEP 678](https://peps.python.org/pep-0678/) (landed in Python 3.11) introduced a new method `add_note` for `BaseException` class. You can call it on any exception to provide additional context which will be shown at the end of the traceback for the exception:

```python
try:
  1/0
except Exception as e:
  e.add_note('oh no!')
  raise
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# ZeroDivisionError: division by zero
# oh no!
```

The PEP gives a good example of how it can be useful. The [hypothesis](https://github.com/HypothesisWorks/hypothesis) library includes in the traceback the arguments that caused the tested code to fail.
