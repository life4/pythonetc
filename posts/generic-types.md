---
published: 2020-06-09
id: 569
author: orsinium
pep: 585
python: "3.9"
---

# generic built-in types (PEP-585)

More cool things from Python 3.9. [PEP-585](https://www.python.org/dev/peps/pep-0585/) introduced generic types support for the built-in types:

```python
# before 3.9:
from typing import List, Type
lst: List[int] = [1, 2, 3]
t: Type[int] = float

# from python 3.9:
lst: list[int] = [1, 2, 3]
t: type[int] = float
```

So, now, `from typing` import will become much shorter! Hooray! The next step would be to support `int & str` instead of `Union[int, str]`.

The only purpose of these types is type annotations. They don't make any runtime type checks:

```python
list[str]({1, 2, 3})
# [1, 2, 3]

isinstance([1, 2, 3], list[str])
# TypeError: isinstance() arg 2 cannot be a parameterized generic
```
