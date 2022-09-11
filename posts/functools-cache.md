---
published: 2020-12-17
id: 641
author: orsinium
qname: functools.cache
python: "3.9"
---

# functools.cache

The decorator `functools.lru_cache` named so because of the underlying cache replacement policy. When the cache size limit is reached [Least Recently Used](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_.28LRU.29) records removed first:

```python
from functools import lru_cache

@lru_cache(maxsize=2)
def say(phrase):
  print(phrase)

say('1')
# 1

say('2')
# 2

say('1')

# push a record out of the cache
say('3')
# 3

# '1' is still cached since it was used recently
say('1')

# but '2' was removed from cache
say('2')
# 2
```

To avoid the limit, you can pass `maxsize=None`:

```python
@lru_cache(maxsize=None)
def fib(n):
  if n <= 2:
    return 1
  return fib(n-1) + fib(n-2)

fib(30)
# 832040

fib.cache_info()
# CacheInfo(hits=27, misses=30, maxsize=None, currsize=30)
```

Python 3.9 introduced `functools.cache` which is the same as `lru_cache(maxsize=None)` but a little bit faster because it doesn't have all that LRU-related logic inside:

```python
from functools import cache

@cache
def fib_cache(n):
  if n <= 2:
    return 1
  return fib(n-1) + fib(n-2)

fib_cache(30)
# 832040

%timeit fib(30)
# 63 ns ± 0.574 ns per loop

%timeit fib_cache(30)
# 61.8 ns ± 0.409 ns per loop
```
