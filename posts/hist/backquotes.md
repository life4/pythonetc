---
published: 02 June 2020, 18:00
author: orsinium
---

# backquotes

Python from the very first release and until Python 2.7 supported backquotes as a shortcut for `repr(...)`:

```python
>>> a = 1
>>> `a + 2`
'3'
>>> `int`
"<type 'int'>"
```

In Python 3, it was removed because it's easy to confuse with single quotes and hard to type on some keyboards.
