---
author: orsinium
pep: 675
python: "3.11"
traces:
  - [module: typing, type: LiteralString]
---

# typing.LiteralString

[PEP 675](https://peps.python.org/pep-0675/) (landed in Python 3.11) introduced a new type `typing.LiteralString`. It matches any `Literal` type, which is the type for explicit literals and constants in the code. The PEP shows a very good example of how it can be used to implement a SQL driver with protection on the type-checker level against SQL injections:

```python
from typing import LiteralString, Final

def run_query(sql: LiteralString): ...

run_query('SELECT * FROM students')  # ok

ALL_STUDENTS: Final = 'SELECT * FROM students'
run_query(ALL_STUDENTS)  # ok

arbitrary_query = input()
run_query(arbitrary_query) # type error, don't do that
```
