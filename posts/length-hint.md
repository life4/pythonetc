---
published: 2018-05-06
id: 81
author: pushtaev
---

# `__length_hint__`

[PEP 424](https://www.python.org/dev/peps/pep-0424/) allows generators and other iterable objects that don't have the exact predefined size to expose a length hint.
For example, the following generator will likely return ~50 elements:

```python {hide}
from random import random
```

```python {continue}
(x for x in range(100) if random() > 0.5)
```

If you write an iterable and want to add the hint, define the `__length_hint__` method. If the length is known for sure, use `__len__` instead.

If you use an iterable and want to know its expected length, use `operator.length_hint`.
