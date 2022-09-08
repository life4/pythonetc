---
published: 28 May 2020, 18:00
author: orsinium
qname: str.removeprefix
pep: 616
---

# str.removeprefix

In python 3.9, [PEP-616](https://www.python.org/dev/peps/pep-0616/) introduced `str.removeprefix` and `str.removesuffix` methods:

```python
'abcd'.removeprefix('ab')
# 'cd'

'abcd'.removeprefix('fg')
# 'abcd'
```

The implementation is simple (it's implemented on C, of course, but the idea is the same):

```python
def removeprefix(self: str, prefix: str) -> str:
    if self.startswith(prefix):
        return self[len(prefix):]
    return self
```
