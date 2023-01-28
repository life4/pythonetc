---
published: 2018-06-04
id: 108
author: pushtaev
---

# C3 MRO

Consider the following class hierarchy:

```python
class GrandParent:
    pass

class Parent1(GrandParent):
    pass

class Parent2(GrandParent):
    pass

class Child(Parent1, Parent2):
    pass
```

Which order will be used to look up the `Child.x()` method?
The naive approach is to recursively search through all parent classes which gives us `Child, Parent1, GrandParent, Parent2`.
While many programming languages follow this method indeed, it doesn't quite make sense, because `Parent2` is more specific than `GrandParent` and should be looked up first.

In order to fix that problem, Python uses C3 superclass linearization, the algorithm that always searches for a method in all child classes before looking up the parent one:

```ipython {continue} {python-interactive-no-check} {# ipython's way of displaying tuples of classes is super custom #}
In : Child.__mro__
Out:
(__main__.Child,
 __main__.Parent1,
 __main__.Parent2,
 __main__.GrandParent,
 object)
```
