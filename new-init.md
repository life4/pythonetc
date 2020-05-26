Creation of class instance is done by `__call__` method of `object` class (provided by metaclass `type`) and practically includes only 2 steps:

1. Call the `__new__` method to create an instance.
2. Call the `__init__` method to set up the instance.

```python
class A:
  def __new__(cls, *args):
    print('new', args)
    return super().__new__(cls)

  def __init__(self, *args):
    print('init', args)

A(1)
# new (1,)
# init (1,)

A.__call__(1)
# new (1,)
# init (1,)
```

So, if you want to create an instance without executing `__init__`, just call `__new__`:

```python
A.__new__(A, 1)                                                                         
# new (1,)
```

Of course, that's a bad practice. The good solution is to avoid a heavy logic in `__init__` so nobody wants to avoid calling it.
