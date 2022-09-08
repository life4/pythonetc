---
published: 02 July 2020, 18:00
author: orsinium
---

# class body

The class body is the same as, let's say, the function body, [with only a few limitations](https://t.me/pythonetc/438). You can put any statements inside, reuse previous results and so on:

```python
class A:
    print('hello')
    a = 1
    if a:
      b = a + 1
# hello

A.b
# 2
```
