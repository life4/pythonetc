# `__init_subclass__` (PEP-487)

Published: 07 July 2020, 18:00

Python 3.6 introduced a few hooks to simplify things that could be done before only with metaclasses. Thanks to [PEP-487](https://www.python.org/dev/peps/pep-0487/). The most useful such hook is `__init_subclass__`. It is called on subclass creation and accepts the class and keyword arguments passed next to base classes. Let's see an example:

```python
speakers = {}

class Speaker:
  # `name` is a custom argument
  def __init_subclass__(cls, name=None):
    if name is None:
      name = cls.__name__
    speakers[name] = cls

class Guido(Speaker): pass
class Beazley(Speaker, name='David Beazley'): pass

speakers
# {'Guido': __main__.Guido, 'David Beazley': __main__.Beazley}
```
