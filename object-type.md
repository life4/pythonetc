Every class is an instance of its metaclass. The default metaclass is `type`. You can use this knowledge to check if something is a class or is an instance:

```python
class A: pass
isinstance(A, type)   # True
isinstance(A(), type) # False
```

However, class and instance are both an instance of `object`!

```python
isinstance(A(), object) # True
isinstance(A, object)   # True
```

This is because `type` an instance of `object` and subclass of `object` at the same time, and `object` is an instance of `type` and has no parent classes.

```python
isinstance(type, object) # True
issubclass(type, object) # True
type(type)      # type
type(object)    # type
type.__mro__    # (type, object)
object.__mro__  # (object,)
```
