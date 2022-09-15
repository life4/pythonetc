---
published: 2020-07-02
id: 577
author: orsinium
traces:
 - [{keyword: class}]
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
