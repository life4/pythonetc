---
published: 2018-04-10
id: 49
author: pushtaev
buttons:
- title: Example online
  url: "https://replit.com/@VadimPushtaev/sliceview"
---

# Slice view

The default list slice in Python creates a copy. It may be undesirable if a slice is too big to be copied, you want a slice to reflect changes in the list, or even want to modify a slice to affect the original object.

To solve the problem with copying a lot of data, one can use `itertools.islice`. It lets you iterate over the part of the list, but doesn't support indexing or modification.

The way to have a class for modifiable slices is to create it. Luckily Python provides the suitable abstract base class: `collections.abc.MutableSequence` (just `collections.MutableSequence` in Python 2). You only need to override `__getitem__`, `__setitem__`, `__delitem__`, `__len__` and `insert`.

The example below doesn't support deletion and inserting, but supports slicing slices and modifications.
