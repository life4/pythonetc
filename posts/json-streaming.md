---
published: 2018-03-30
id: 32
author: pushtaev
---

# JSON streaming

Sometimes you need to create JSON from a big pile of data you can stream
from some source, file or socket for instance.
Sadly you can't encode generator as-is using the Python `json` library:

```python {hide}
import json
```

```ipython {continue} {no-run}
In [1]: json.dumps(range(10))
...
TypeError: Object of type 'range' is not JSON serializable
```

The simple solution here is to derive from `list` and override `__iter__` method:

```ipython {continue}
In [1]: class LazyList(list):
   ...:     def __init__(self, gen):
   ...:         self.__gen = gen
   ...:
   ...:     def __iter__(self):
   ...:         return iter(self.__gen)
   ...:
   ...:
In [2]: json.dumps(LazyList(range(10)))
Out[2]: '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
```

Mind that the solution is not problem-free.
It might not work correctly for `indent` parameter,
and also some versions of `json` require you to override `__len__` as well.

The solution described is a more or less hack,
the clear one is to use `simplejson` instead.
It explicitly supports `iterable_as_array` flag:

```ipython
In [1]: import simplejson as json
In [2]: json.dumps(range(10), iterable_as_array=True)
Out[3]: '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
```

You also may put all data of the generator into a list and encode it afterward but will take some time and additional memory.
