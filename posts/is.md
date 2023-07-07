---
published: 2022-08-16
id: 693
author: orsinium
traces:
  - [keyword: is]
---

# is

The operator `is` checks if the two given objects are the same object in the memory:

```python
{} is {}  # False
d = {}
d is d    # True
```

Since types are also objects, you can use it to compare types:

```python
type(1) is int        # True
type(1) is float      # False
type(1) is not float  # True
```

And you can also use `==` for comparing types:

```python
type(1) == int  # True
```

So, when to use `is` and when to use `==`? There are some best practices:

+ Use `is` to compare with `None`: `var is None`.
+ Use `is` to compare with `True` and `False`. However, don't explicitly check for `True` and `False` in conditions, prefer just `if user.admin` instead of `if user.admin is True`. Still, the latter can be useful in tests: `assert actual is True`.
+ Use `isinstance` to compare types: `if isinstance(user, LoggedInUser)`. The big difference is that it allows subclasses. So if you have a class `Admin` which is subclass of `LoggedInUser`, it will pass `isinstance` check.
+ Use `is` in some rare cases when you explicitly want to allow only the given type without subclasses: `type(user) is Admin`. Keep in mind, that `mypy` will refine the type only for `isinstance` but not for `type is`.
+ Use `is` to compare [enum](https://docs.python.org/3/library/enum.html) members: `color is Color.RED`.
+ Use `==` in ORMs and query builders like [sqlalchemy](https://www.sqlalchemy.org/): `session.query(User).filter(User.admin == True)`. The reason is that `is` behavior cannot be redefined using magic methods but `==` can (using `__eq__`).
+ Use `==` in all other cases. In particular, always use `==` to compare values: `answer == 42`.
