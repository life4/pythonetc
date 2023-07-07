---
published: 2023-02-28
author: orsinium
topics:
  - packaging
pep: 517
depends_on:
  - pyproject-toml
---

# build-system

[PEP-517](https://peps.python.org/pep-0518/) and [PEP-518](https://peps.python.org/pep-0518/) introduced the `build-system` section in `pyproject.toml` that tells package management tools (like pip) how to build wheel distributions for the project. For example, this is the section if you use flit:

```toml
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"
```

It tells pip to install `flit_core` of the given version and then call callbacks inside `flit_core.buildapi`, which should build the distribution for the project.

Having this section allows pip to build and install any Python project from the source, doesn't matter what build system it uses. Before the PEP, tools like poetry and flit had to generate a special `setup.py` file for pip to be able to install the project from the source (or a non-wheel tarball distribution).
