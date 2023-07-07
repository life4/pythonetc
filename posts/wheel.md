---
published: 2023-02-14
author: orsinium
topics:
  - packaging
pep: 427
---

# wheel

[PEP 427](https://peps.python.org/pep-0427/) introduced (and [PEP 491](https://peps.python.org/pep-0491/) improved) a new format for Python distributions called "wheel".

Before the PEP, Python distributions were just tar.gz archives containing the source code of the library distributed, some additional files (`README.rst`, `LICENSE`, sometimes tests), and `setup.py` file. To install the library from the distribution, pip had to download the archive, extract it into a temporary directory, and execute `python setup.py install` to install the package.

Did it work? Well, kind of. It works well enough for pure Python packages, but if the package has C code, it had to be built on the target machine each time the package needs to be installed, because the built binary highly depends on the target OS, architecture, and Python version.

The new wheel format allows to significantly speed up the process. It changed 2 significant things:

1. The file name for wheel packages is standardized. It contains the name and version of the package, the required minimal version (2.7, 3.8), the type (CPython, PyPy) of the Python interpreter, OS name, architecture, and ABI version. For example, `flask-1.0.2-py2.py3-none-any.whl` says "it is flask package version 1.0.2 for both Python 2 and 3, any ABI, and any OS". That means, Flask is a pure Python package, so can be installed anywhere. Or `psycopg2-2.8.6-cp310-cp310-linux_x86_64.whl` says "it is psycopg2 version 2.8.6 for CPython 3.10 Linux 64bit". That means psycopg2 has some prebuild C libraries for a very specific environment. The package can have multiple wheel distributions per version, and pip will pick and download the one that is made for you.
2. Instead of `setup.py`, the archive (which is now zip instead of tar.gz) contains already parsed metadata. So, to install the package, it's enough to just extract it into site-packages directory, no need to execute anything.

Currently, the wheel distribution format is well-adopted and [available for almost all modern packages](https://pythonwheels.com/).

When you create a new virtual environment, make sure you have the latest version of setuptools for tarballs, and the latest version of the `wheel` package for wheels. No, really, do it. The `wheel` package is not installed by default in the new venvs, and without it, installation of some packages will be slow and painful.

```bash
python3 -m venv .venv
.venv/bin/pip install -U pip setuptools wheel
```
