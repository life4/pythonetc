---
published: 2022-07-19
id: 689
author: orsinium
topics:
  - typing
traces:
  - [{module: __future__}, {function: annotations}]
pep: 563
python: "3.7"
---

# `from __future__ import annotations` (PEP-563)

[PEP-563](https://www.python.org/dev/peps/pep-0563/) (landed in Python 3.7) introduced postponed evaluation of type annotations. That means, all your type annotations aren't executed at runtime but rather considered strings.

The initial idea was to make it the default behavior in Python 3.10 but it was postponed after a negative reaction from the community. In short, it would be in some cases impossible to get type information at runtime which is crucial for some tools like [pydantic](https://github.com/samuelcolvin/pydantic) or [typeguard](https://github.com/agronholm/typeguard). For example, see [pydantic#2678](https://github.com/samuelcolvin/pydantic/issues/2678).

Either way, starting from Python 3.7, you can activate this behavior by adding `from __future__ import annotations` at the beginning of a file. It will improve the import time and allow you to use in annotations objects that aren't defined yet.

For example:

```python
class A:
  @classmethod
  def create(cls) -> A:
    return cls()
```

This code will fail at import time:

```python
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    class A:
  File "tmp.py", line 3, in A
    def create(cls) -> A:
NameError: name 'A' is not defined
```

Now add the magic import, and it will work:

```python
from __future__ import annotations

class A:
  ...
```

Another solution is to manually make annotations strings. So, instead of `-> A:` you could write `-> 'A':`.
