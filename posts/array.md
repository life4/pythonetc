---
published: 2020-12-10
id: 639
author: orsinium
traces:
  - [module: array]
---

# array performance

The module [array](https://t.me/pythonetc/124) is helpful if you want to be memory efficient or interoperate with C. However, working with array can be slower than with list:

```python
import random
import array
lst = [random.randint(0, 1000) for _ in range(100000)]
arr = array.array('i', lst)

%timeit for i in lst: pass
# 1.05 ms ± 1.61 µs per loop

%timeit for i in arr: pass
# 2.63 ms ± 60.2 µs per loop

%timeit for i in range(len(lst)): lst[i]
# 5.42 ms ± 7.56 µs per loop

%timeit for i in range(len(arr)): arr[i]
# 7.8 ms ± 449 µs per loop
```

The reason is that `int` in Python is a [boxed object](https://en.wikipedia.org/wiki/Object_type#Boxing), and wrapping raw integer value into Python `int` takes some time.
