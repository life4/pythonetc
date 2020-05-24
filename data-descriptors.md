[Descriptors](https://docs.python.org/3/howto/descriptor.html) are special class attributes with a custom behavior on attribute get, set, or delete. If an object defines `__set__` or `__delete__`, it is considered a data descriptor. Descriptors that only define `__get__` are called non-data descriptors. The difference is that non-data descriptors are called only if the attribute isn't presented in `__dict__` of the instance.

Non-data descriptor:

```python
class D:
  def __get__(self, obj, owner):
    print('get', obj, owner)

class C:
    d = D()

c = C()
c.d
# get <__main__.C object at 0x7fdcec49ceb8> <class '__main__.C'>

# updating __dict__ shadows the descriptor
c.__dict__['d'] = 1
c.d
# 1
```

Data descriptor:

```python
class D:
  def __get__(self, obj, owner):
    print('get', obj, owner)

  def __set__(self, obj, owner):
    print('set', obj, owner)

class C:
    d = D()

c = C()
c.d
# get <__main__.C object at 0x7fdcec49ceb8> <class '__main__.C'>

# updating __dict__ doesn't shadow the descriptor
c.__dict__['d'] = 1
c.d
# get <__main__.C object at 0x7fdcec49ceb8> <class '__main__.C'>
```
