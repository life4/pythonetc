---
published: 2020-12-15
author: orsinium
qname: functools.lru_cache
python: "3.2"
---

# functools.lru_cache

Decorator [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) caches the function result based on the given arguments:

```python
from functools import lru_cache
@lru_cache(maxsize=32)
def say(phrase):
  print(phrase)
  return len(phrase)

say('hello')
# hello
# 5

say('pythonetc')
# pythonetc
# 9

# the function is not called, the result is cached
say('hello')
# 5
```

The only limitation is that all arguments must be [hashable](https://t.me/pythonetc/157):

```python
say({})
# TypeError: unhashable type: 'dict'
```

The decorator is useful for recursive algorithms and costly operations:

```python
@lru_cache(maxsize=32)
def fib(n):
  if n <= 2:
    return 1
  return fib(n-1) + fib(n-2)

fib(30)
# 832040
```

Also, the decorator provides a few helpful methods:

```python
fib.cache_info()
# CacheInfo(hits=27, misses=30, maxsize=32, currsize=30)

fib.cache_clear()
fib.cache_info()
# CacheInfo(hits=0, misses=0, maxsize=32, currsize=0)

# Introduced in Python 3.9:
fib.cache_parameters()
# {'maxsize': None, 'typed': False}
```

And the last thing for today, you'll be surprised how fast `lru_cache` is:

```python
def nop():
    return None

@lru_cache(maxsize=1)
def nop_cached():
    return None

%timeit nop()
# 49 ns ± 0.348 ns per loop

# cached faster!
%timeit nop_cached()
# 39.3 ns ± 0.118 ns per loop
```
