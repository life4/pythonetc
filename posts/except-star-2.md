---
author: orsinium
traces:
  - [{exception: ExceptionGroup}]
pep: 654
python: "3.11"
---

# `except*` for regular exceptions

One more thing you should know about `except*`. It can match not only sub-exceptions from `ExceptionGroup` but regular exceptions too. And for simplicity of handling, regular exceptions will be wrapped into `ExceptionGroup`:

```python
try:
  raise KeyError
except* KeyError as e:
  print('caught:', repr(e))
# caught: ExceptionGroup('', (KeyError(),))
```
