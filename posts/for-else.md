---
published: 2018-05-09
id: 84
author: pushtaev
---

# `else` in loops

In Python, an `else` block could be presented not only after `if`,
but after `for` and `while` as well. The code inside `else` is executed *unless* the loop was interrupted by `break`.

The common usage for this is to search something in a loop and use `break` when found:

```ipython
In : first_odd = None
In : for x in [2,3,4,5]:
...:     if x % 2 == 1:
...:         first_odd = x
...:         break
...: else:
...:     raise ValueError('No odd elements in list')
...:
In : first_odd
Out: 3
```

```ipython {merge} {continue} {shield:ValueError}
In : for x in [2,4,6]:
...:     if x % 2 == 1:
...:         first_odd = x
...:         break
...: else:
...:     raise ValueError('No odd elements in list')
...:
...
ValueError: No odd elements in list
```
