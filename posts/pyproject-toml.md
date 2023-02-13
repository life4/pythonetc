---
published: 2023-02-21
author: orsinium
topics:
  - packaging
pep: 518
---

# pyproject.toml

[PEP-518](https://peps.python.org/pep-0518/) introduced changes not in Python itself but rather in its ecosystem. The idea is pretty simple: let's store configs for all tools in `pyproject.toml` file, in `tool.TOOL_NAME` section. For example, for [mypy](https://mypy.readthedocs.io/):

```toml
[tool.mypy]
files = ["my_project"]
python_version = 3.8
```

At this moment, almost all popular tools support `pyproject.toml` as the configuration file, in one way or another: mypy, pytest, coverage, isort, bandit, tox, etc. The only exception from the tooling I know is flake8.

Before `pyproject.toml`, many tools used to use `setup.cfg` for the same purpose, but this format (INI) has a few disadvantages compared to TOML: it's not well-standardized, and the only supported type of values is string.
