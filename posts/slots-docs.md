---
published: 2020-11-05
author: orsinium
python: "3.8"
---

# dict as `__slots__`

`__slots__` [can be used to save memory](https://t.me/pythonetc/233). You can use any iterable as `__slots__` value, including `dict`. And starting from Python 3.8, you can use `dict` to specify docstrings for slotted attributes `__slots__`:

```python
class Channel:
  "Telegram channel"
  __slots__ = {
    'slug': 'short name, without @',
    'name': 'user-friendly name',
  }
  def __init__(self, slug, name):
    self.slug = slug
    self.name = name

inspect.getdoc(Channel.name)
# 'user-friendly name'
```

Also, `help(Channel)` lists docs for all slotted attributes:

```python
class Channel(builtins.object)
 |  Channel(slug, name)
 |
 |  Telegram channel
 |
 |  Methods defined here:
 |
 |  __init__(self, slug, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  name
 |      user-friendly name
 |
 |  slug
 |      short name, without @
```
