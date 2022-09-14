---
published: 2022-01-04
author: orsinium
topics:
  - builtin
  - function
qname: zip
pep: 618
python: "3.10"
---

# zip

[zip](https://docs.python.org/3/library/functions.html#zip) function allows you to iterate over multiple iterators at the same time (I know you know it, just bear with me):

```python
list(zip([1, 2], [3, 4]))
# [(1, 3), (2, 4)]
```

But what if the given iterators have a different length? Then the resulting iterator will have the shortest length:

```python
list(zip([1, 2], [3, 4, 5]))
# [(1, 3), (2, 4)]
```

If you need all values, there is `itertools.zip_longest`:

```python
from itertools import zip_longest
list(zip_longest([1, 2], [3, 4, 5], fillvalue=None))
# [(1, 3), (2, 4), (None, 5)]
```

But what if you want to ensure that both iterators have the same length? For that purpose, [PEP-618](https://www.python.org/dev/peps/pep-0618/) (landed in Python 3.10) introduced `strict` flag:

```python
list(zip([1, 2], [3, 4, 5], strict=True))
# ValueError: zip() argument 2 is longer than argument 1
```
