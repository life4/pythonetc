---
published: 2020-06-23
author: orsinium
qname:
    - sys.getrecursionlimit
    - sys.setrecursionlimit
---

# sys.setrecursionlimit

Python doesn't support [tail recursion](https://t.me/pythonetc/239). Hence, it's easy to face `RecursionError` when implementing recursive algorithms. You can get and change maximum recursion depth with [sys.getrecursionlimit](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit) and [sys.setrecursionlimit](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit) functions:

```python
sys.getrecursionlimit()
# 3000

sys.setrecursionlimit(4000)
sys.getrecursionlimit()
# 4000
```

However, it's a dangerous practice, especially because every new frame on the call stack is quite expensive. Luckily, any recursive algorithm can be rewritten with iterations.
