---
published: 2022-08-02
id: 691
author: orsinium
topic:
  - stdlib
  - typing
  - type
qname: typing.Union
pep: 604
python: "3.10"
---

# Union alias (PEP-604)

[PEP-604](https://www.python.org/dev/peps/pep-0604/) (landed in Python 3.10) introduced a new short syntax for `typing.Union` ([as I predicted](https://t.me/pythonetc/569), but I messed up union with intersection, shame on me):

```python
def greet(name: str) -> str | None:
  if not name:
    return None
  return f"Hello, {name}"
```

You already can use it in older Python versions by adding `from __future__ import annotations`, type checkers will understand you.
