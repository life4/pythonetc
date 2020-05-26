Try to avoid getting dunder attributes directly. Python provides helper functions for getting of of standard dunder attributes:

- `type(self)` instead of `self.__class__`
- `inspect.getdoc(cls)` instead of `cls.__doc__`
- `vars(obj)` instead of `obj.__dict__`
- `cls.mro()` instead of `cls.__mro__`
