---
published: 2018-05-08
id: 83
author: pushtaev
---

# itertools.chain

The `itertools.chain` function is a way to iterate over many iterables as though they are glued together:

```python {hide}
from itertools import chain
```

```ipython {continue}
In : list(chain(['a', 'b'], range(3), 'xyz'))
Out: ['a', 'b', 0, 1, 2, 'x', 'y', 'z']
```

Sometimes you want to know whether a generator is empty (rather say, exhausted). To do this, you have to try getting the next element from the generator. If it works, you would like to put element back in the generator, which of course is not possible. You can glue it back with `chain` instead:

```python {continue}
def sum_of_odd(gen):
    try:
        first = next(gen)
    except StopIteration:
        raise ValueError('Empty generator')

    return sum(
        x for x in chain([first], gen)
        if x % 2 == 1
    )
```

Usage example:

```ipython {continue}
In : sum_of_odd(x for x in range(1, 6))
Out: 9
In : sum_of_odd(x for x in range(2, 3))
Out: 0
```

```ipython {merge} {continue} {shield:ValueError}
In : sum_of_odd(x for x in range(2, 2))
...
ValueError: Empty generator
```
