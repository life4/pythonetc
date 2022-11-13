---
published: 2018-03-27
id: 26
author: pushtaev
---

# abc.abstractmethod

The popular method to declare an abstract method in Python is to use `NotImplentedError` exception:

```python
def human_name(self):
    raise NotImplementedError
```

Though it's pretty popular and even has IDE support
(Pycharm consider such method to be abstract) this approach has a downside.
You get the error only upon method call, not upon class instantiation.

Use `abc` to avoid this problem:

```python
from abc import ABCMeta, abstractmethod
class Service(metaclass=ABCMeta):
    @abstractmethod
    def human_name(self):
        pass
```
