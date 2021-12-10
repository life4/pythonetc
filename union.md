# Union alias (PEP-604)

Published: 28 December 2021, 18:00.

[PEP-604](https://www.python.org/dev/peps/pep-0604/) (landed in Python 3.10) introduced a new short syntax for `typing.Union` ([as we predicted](https://t.me/pythonetc/569)):

```python
def greet(name: str) -> str | None:
  if not name:
    return None
  return f"Hello, {name}"
```

You already can use it in older Python versions by adding described in the previous post `from __future__ import annotations`, [mypy](http://mypy-lang.org/) will understand you.
