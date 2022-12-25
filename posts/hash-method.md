---
published: 2018-04-28
id: 72
author: pushtaev
---

# `__hash__`

You can use any object as a dictionary key in Python as long as it implements the `__hash__` method.
This method can return any integer as long as the only requirement is met: equal objects should have equal hashes (not vice versa).

You also should avoid using mutable objects as keys, because once the object becomes not equal to the old self, it can't be found in a dictionary anymore.

There is also one bizarre thing that might surprise you during debugging or unit testing:

```ipython
In : class A:
...:     def __init__(self, x):
...:         self.x = x
...:
...:     def __hash__(self):
...:         return self.x
...:
In : hash(A(2))
Out: 2
In : hash(A(1))
Out: 1
In : hash(A(0))
Out: 0
In : hash(A(-1))  # sic!
Out: -2
In : hash(A(-2))
Out: -2
```

In CPython `-1` is internally reserved for error states, so it's implicitly converted to `-2`.
