---
published: 2018-04-25
id: 68
author: pushtaev
---

# bisect

If you need to search through a sorted collection, binary search is what you need. This simple algorithm compares the target value to the middle of the array; the result determines which half should be searched next.

Python standard library provides a way to use binary search without directly implementing it. `bisect_left` function returns the leftmost position in a sorted list for the element, while `bisect_right` return the rightmost one.

```ipython
In : from random import randrange
In : from bisect import bisect_left
In : n = 1000000
In : look_for = 555555
In : lst = sorted(randrange(0, n) for _ in range(n))
```

```ipython {ipython-native} {continue} {merge}
In : %timeit look_for in lst
69.7 ms ± 449 µs per loop
In : %timeit look_for == lst[bisect_left(lst, look_for)]
927 ns ± 2.28 ns per loop
```
