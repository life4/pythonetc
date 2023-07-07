---
published: 2018-03-28
id: 28
author: pushtaev
sequence: heapq
buttons:
- title: More advanced example live
  url: "https://replit.com/@VadimPushtaev/heapq"
---

# heapq

A _priority queue_ is a data structure that supports two operations:
add element and extract the minimum of all elements among previously added.

One of the most common implementations of a priority queue is a _binary heap_.
It's a [complete binary tree](https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees) with the following property:
the key stored in each node is equal to or less than (≤) the keys in the node's children.
The minimum of all elements is a root of such tree.

```text
              1

      3               7

  5       4       9       8

15 16   17 18   19
```

In a binary heap, both inserting and extraction operations' complexity is _O(log n)_.

The common way of storing a complete binary tree in memory is an array, where children of `x[i]` are `x[2*i+1]` and `x[2*i+2]`:

```python
[1, 3, 7, 5, 4, 9, 8, 15, 16, 17, 18, 19]
```

Python doesn't provide a binary heap as a class,
but it does provide a number of functions that treat `list` like a binary heap.
They are placed in the [heapq module](https://docs.python.org/3.0/library/heapq.html).

```ipython
In [1]: from heapq import *
In [2]: heap = [3,2,1]
In [3]: heapify(heap)
In [4]: heap
Out[4]: [1, 2, 3]
In [5]: heappush(heap, 0)
In [6]: heap
Out[6]: [0, 1, 3, 2]
In [7]: heappop(heap)
Out[7]: 0
In [8]: heap
Out[8]: [1, 2, 3]
```
