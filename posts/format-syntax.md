---
published: 2018-05-04
id: 78
author: pushtaev
---

# `format` syntax

The `format` method of Python string is a mighty tool that supports a lot of things that you are probably not even aware of.
Each replacement placeholder (`{...}`) may contain three parts: field name, conversion and format specification.

The *field name* is used to specify which argument exactly should be used as a replacement:

```python-interactive
>>> '{}'.format(42)
'42'
>>> '{1}'.format(1, 2)
'2'
>>> '{y}'.format(x=1, y=2)
'2'
```

The *conversion* let you ask `format` to use `repr()` (or `ascii()`) instead of `str()` while converting objects to strings:

```python {hide}
from datetime import datetime
```

```python-interactive {python-interactive-no-check} {continue}
>>> '{!r}'.format(datetime.now())
'datetime.datetime(2018, 5, 3, 23, 48, 49, 157037)'
>>> '{}'.format(datetime.now())
'2018-05-03 23:49:01.060852'
```

Finally, the *format specification* is a way to define how values are presented:

```python-interactive
>>> '{:+,}'.format(1234567)
'+1,234,567'
>>> '{:>19}'.format(1234567)
'            1234567'
```

This specification may be applied to a single object with `format` function (not the `str` method):

```python
format(5000000, '+,')
'+5,000,000'
```

The `format` function calls `__format__` method of the object internally, so you can alter its behavior for your types.
