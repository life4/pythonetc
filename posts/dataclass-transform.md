---
author: orsinium
published: 2022-12-06
pep: 681
python: "3.11"
traces:
  - [module: typing, decorator: dataclass_transform]
---

# typing.dataclass_transform

[PEP 681](https://peps.python.org/pep-0681/) (landed in Python 3.11) introduced `typing.dataclass_transform` decorator. It can be used to mark a class that behaves like a dataclass. The type checker will assume that it has `__init__` that accepts annotated attributes as arguments, `__eq__`, `__ne__`, and `__str__`. For example, it can be used to annotate [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) or [Django](https://github.com/django/django) models, [attrs](https://github.com/python-attrs/attrs) classes, [pydantic](https://github.com/pydantic/pydantic) validators, and so on. It's useful not only for libraries that don't provide a mypy plugin but also if you use a non-mypy type checker. For instance, [pyright](https://github.com/microsoft/pyright), which is used by vscode Python plugin to show types, highlight syntax, provide autocomplete, and so on.
