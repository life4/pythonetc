---
author: orsinium
published: 2022-11-17
traces:
  - [{exception: ExceptionGroup}]
pep: 654
python: "3.11"
depends_on:
  - except-star
  - exception-group
---

# `except*` for regular exceptions

There is one more thing you should know about `except*`. It can match not only sub-exceptions from `ExceptionGroup` but regular exceptions too. And for simplicity of handling, regular exceptions will be wrapped into `ExceptionGroup`:

```python
try:
  raise KeyError
except* KeyError as e:
  print('caught:', repr(e))
# caught: ExceptionGroup('', (KeyError(),))
```
