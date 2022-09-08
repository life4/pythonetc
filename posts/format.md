---
published: 2020-09-08
author: orsinium
qname: format
---

# format

There is a built-in function `format` that basically just calls `__format__` method of the passed argument type with passed spec. It is used in `str.format` as well.

```python
class A:
    def __format__(self, spec):
        return spec

format(A(), 'oh hi mark')
# 'oh hi mark'

'{:oh hi mark}'.format(A())
# 'oh hi mark'
```
