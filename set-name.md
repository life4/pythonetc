If you're going to store data in the descriptor, the reasonable question is "where".

1. If data stored in the descriptor's attribute, it will be shared between all instances of the class where the descriptor is assigned.
2. If data is stored in a dict inside of the descriptor, where the key is hash of class and value is data, it will lead to a memory leak.

So, the best solution is to store data in the class itself. But how to name the attribute?

`@cached_property` that we implemented above, relies on the passed function name and it is wrong:

```python
class C:
    @cached_property
    def a(self):
        print('called')
        return 1
    b = a
c = C()

# `a` is cached:
c.a
# called
# 1
c.a
# 1

# but `b` isn't:
c.b
# called
# 1
c.b
# called
# 1
```

[PEP-487](https://www.python.org/dev/peps/pep-0487/) introduced `__set_name__` hook. It is called on descriptor assignment to a class attribute and accepts the class itself at the name of the attribute. Let's use it and fix the implementation:

```python
class cached_property:
  def __init__(self, func):
    self.func = func

  def __set_name__(self, owner, name):
    self.name = name

  def __get__(self, obj, cls):
    if obj is None:
      return self
    # we've replaced `self.func.__name__` by `self.name` here
    value = obj.__dict__[self.name] = self.func(obj)
    return value
```
