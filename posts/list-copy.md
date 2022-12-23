---
published: 2018-04-18
id: 59
author: pushtaev
---

# List copy

When you want to empty a list in Python, you probably do `lst = []`.
In fact, you just create a new empty list and assign it to `lst`, while all others owners of the same list still have the same content:

```ipython
In : lst = [1, 2, 3]
In : lst2 = lst
In : lst = []
In : lst2
Out: [1, 2, 3]
```

While this may seem pretty obvious, the correct solution wasn't straightforward until `lst.clear()` was introduced in Python 3.3.

Before that, you should do `del lst[:]` or `lst[:] = []`. It works since slice syntax allows you to modify part of the list, and that *part* is the whole list in case of `[:]`.
