---
published: 2018-03-29
id: 31
author: pushtaev
buttons:
- title: Try the code live
  url: "https://replit.com/@VadimPushtaev/getattr"
---

# getattr VS getattribute

Python data model contains two methods with similar names:
`__getattr__` and `__getattribute__`.
The key difference is that `__getattribute__` is called unconditionally
on an every attribute access,
but `__getattr__` is only called when `__getattribute__` fails
to find an attribute (raises `AttributeError`).

The default `__getattribute__` behavior (the one you use every day)
is to return the attribute if it exists or to raise `AttributeError`.
There are no default for `__getattr__`.

That actually means that by default `__getattr__` is a way to handle attributes
that couldn't be found by ordinary means.
That can be helpful for some sorts of metaprogramming or creating DSLs.

With this code you can get `hex` version of any attribute
by prepending `hex_` to its name
(that's not really helpful but good enough as an example):

```python {no-print}
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __getattr__(self, attr):
        prefix, orig_attr = attr.split('_', 2)
        if prefix == 'hex' and hasattr(self, orig_attr):
            return hex(getattr(self, orig_attr))
        else:
            raise AttributeError

p = Point(16, 20)
print(p.hex_x, p.hex_y)
```

There are also `__setattr__` and `__delattr__` methods for setting and deleting attributes, and they both are called unconditionally. That means that the `__getattr__` method stands out here, not `__getattrbiute__` like it may seem.
