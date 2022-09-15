---
published: 2021-04-06
id: 659
author: orsinium
traces:
  - [{module: copy}, {function: deepcopy}]
---

# copy.deepcopy

What if we want to modify a collection inside a function but don't want these modifications to affect the caller code? Then we should explicitly copy the value.

For this purpose, all mutable built-in collections provide method `.copy`:

```python
def f(v2):
  v2 = v2.copy()
  v2.append(2)
  print(f'{v2=}')
  # v2=[1, 2]
v1 = [1]
f(v1)
print(f'{v1=}')
# v1=[1]
```

Custom objects (and built-in collections too) can be copied using [copy.copy](https://docs.python.org/3/library/copy.html):

```python
import copy

class C:
    pass

def f(v2: C):
  v2 = copy.copy(v2)
  v2.p = 2
  print(f'{v2.p=}')
  # v2.p=2

v1 = C()
v1.p = 1
f(v1)
print(f'{v1.p=}')
# v1.p=1
```

However, `copy.copy` copies only the object itself but not underlying objects:

```python
v1 = [[1]]
v2 = copy.copy(v1)
v2.append(2)
v2[0].append(3)
print(f'{v1=}, {v2=}')
# v1=[[1, 3]], v2=[[1, 3], 2]
```

So, if you need to copy all subobjects recursively, use, `copy.deepcopy`:

```python
v1 = [[1]]
v2 = copy.deepcopy(v1)
v2[0].append(2)
print(f'{v1=}, {v2=}')
# v1=[[1]], v2=[[1, 2]]
```
