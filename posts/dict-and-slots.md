---
published: 2018-04-02
id: 35
author: pushtaev
---

# __dict__ and __slots__

Objects in Python store their attributes in dictionaries
that can be accessed by `__dict__` magic attribute:

```ipython
In [1]: class A: pass
In [2]: a = A()
In [3]: a.x = 1
In [4]: a.__dict__
Out[4]: {'x': 1}
```

By direct accessing it you can even create attributes
that are not Python identifiers
(which means you can't get them with a standard `obj.attr` syntax):

```ipython {continue}
In [6]: a.__dict__[' '] = ' '
In [7]: getattr(a, ' ')
Out[7]: ' '
```

You can also ask Python to store attributes directly in memory
(like a simple C struct) using `__slots__`.
It will save some memory and some CPU cycles that are used for dictionary lookups.

```python
class Point:
    __slots__ = ['x', 'y']
```

There are some things you should remember while using slots. First, you can't set any attributes that are not specified in `__slots__` (unless you add `__dict__` there as well). Second, if you inherit from a class with slots, your own `__slots__` don't override parental `__slots__` but are added to it:

```python {continue}
class Parent: __slots__ = ['x']
class Child(Parent): __slots__ = ['y']
c = Child()
c.x = 1
c.y = 2
```

```python {continue} {hide}
assert c.x == 1
assert c.y == 2
```

Third, you can't inherit from two different classes with nonempty `__slots__`,
even if they are identical.
You can get more information from this
[excellent Stack Overflow answer](https://stackoverflow.com/a/28059785/1102638).

Remember, that `__slots__` is meant for optimization,
not for constraining attributes.
