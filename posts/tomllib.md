---
published: 2023-03-07
author: orsinium
traces:
  - [{module: tomllib}]
pep: 680
depends_on:
  - pyproject-toml
---

# tomllib

To recap: PEP-518 introduced pyproject.toml, and many Python tools started to use it to store their configs. The issue, however, is that there is no module in stdlib to parse TOML. So, different tools started to use different third-party packages for the task:

+ [tomli](https://github.com/hukkin/tomli) (used by [mypy](https://mypy.readthedocs.io/)) is a pure Python library that can only read TOML.
+ [toml](https://github.com/uiri/toml) (used by most of the tools) can both read and write TOML.
+ [tomlkit](https://github.com/sdispater/tomlkit) (used by [poetry](https://python-poetry.org/)) can read, write, and modify TOML (preserving the original formatting and comments).

[PEP 680](https://peps.python.org/pep-0680/) (landed in Python 3.11) introduced tomli into stdlib. But why tomli and not another library? It's pure Python and minimalistic. It cannot write TOML files, but reading is enough for most of the tools to work with pyproject.toml. And to avoid unpleasant conflicts when tomli is installed in the same environment, the name of the module was changed to [tomllib](https://docs.python.org/3/library/tomllib.html).
