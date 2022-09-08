---
published: 2020-11-12
author: orsinium
pep: 560
python: "3.7"
---

# `__class_getitem__` (PEP-560)

[PEP-560](https://www.python.org/dev/peps/pep-0560/) (landed in Python 3.7) introduced a new magic method `__class_getitem__`. it is the same as `__getitem__` but for not instancinated class. The main motivation is easier type annotation support for generic collections like `List[int]` or `Type[Dict[str, int]]`:

```python
class MyList:
  def __getitem__(self, index):
    return index + 1

  def __class_getitem__(cls, item):
    return f"{cls.__name__}[{item.__name__}]"

MyList()[1]
# 2

MyList[int]
# 'MyList[int]'
```
