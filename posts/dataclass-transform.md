---
author: orsinium
pep: 681
python: "3.11"
traces:
  - [module: typing, decorator: dataclass_transform]
---

# typing.dataclass_transform

[PEP 681](https://peps.python.org/pep-0681/) introduced `typing.dataclass_transform` decorator. It can be used to mark a class that behaves in a manner similar to a dataclass. The type checker will assume that it has `__init__` that accepts annotated attributes as arguments, `__eq__`, `__ne__`, and `__str__`. For example, it can be used to annotate SQLAlchemy or Django models, attrs classes, pydantic validators, and so on. It's useful not only for libraries that don't provide a mypy plugin but also if you use a non-mypy type checker. For instance, pyright, which is used by vscode Python plugin to show types, highlight syntax, provide autocomplete, and so on.
