---
published: 2020-12-22
id: 642
author: orsinium
topics:
  - stdlib
  - function
qname: re.compile
---

# re.compile

Always precompile regular expressions using `re.compile` if the expression is known in advance:

```python
# generate random string
from string import printable
from random import choice
text = ''.join(choice(printable) for _ in range(10 * 8))

# let's find numbers
pat = r'\d(?:[\d\.]+\d)*'
rex = re.compile(pat)

%timeit re.findall(pat, text)
# 2.08 µs ± 1.89 ns per loop

# pre-compiled almost twice faster
%timeit rex.findall(text)
# 1.3 µs ± 68.8 ns per loop
```

The secret is that module-level `re` functions just compile the expression and call the corresponding method, no optimizations involved:

```python
def findall(pattern, string, flags=0):
    return _compile(pattern, flags).findall(string)
```

If the expression is not known in advance but can be used repeatedly, consider using `functools.lru_cache`:

```python
from functools import lru_cache

cached_compile = lru_cache(maxsize=64)(re.compile)

def find_all(pattern, text):
    return cached_compile(pattern).findall(text)
```
