---
author: pushtaev
id: 12
published: 2018-03-19
sequence: dict-keys
---

# Dict keys

In Python 3 `keys`, `values` and `items` methods of dicts return view objects. They returned lists back in Python 2. The main difference is views don't store all items in memory, but yield them as long as they are requested. It works just fine as long as you are trying to iterate over keys (which you usually are), but you can't access elements by index anymore.

```txt
TypeError: 'dict_keys' object does not support indexing
```

You can argue that you don't really need indexing keys since their order is random, but it's not completely true. First of all, `d.keys()[0]` can be a proper way to get any key (use `next(d.keys())` in Python 3). Second, since Python 3.6 dicts are insertion ordered in CPython and that will be a language feature since Python 3.7.
