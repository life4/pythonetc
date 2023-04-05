---
author: orsinium
traces:
  - [type: str, method: startswith]
  - [type: str, method: endswith]
---

# str.startswith and str.endswith

The `str.startswith` and `str.endswith` methods are used to check if the given string starts with the given prefix and ends with the given suffix respectively:

```python
'abc'.startswith('ab') # True
'abc'.startswith('bc') # False
'abc'.endswith('ab') # False
'abc'.endswith('bc') # True
```

What many people don't know is that both methods can accept a tuple of strings. In that case, they check if any of the prefixes/suffixes match:

```python
'abc'.startswith(('ab', 'cd')) # True
'cde'.startswith(('ab', 'cd')) # True
'def'.startswith(('ab', 'cd')) # False
'abc'.endswith(('bc', 'cd')) # True
```
