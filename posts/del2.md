---
published: 2022-08-30
id: 695
author: orsinium
traces:
  - [type: object, method: __del__]
---

# `__del__`

The method `__del__` is called on the object by the garbage collector when the last reference to the object is removed:

```python
class A:
  def __del__(self):
    print('destroying')

a = b = A()
del a
del b
# destroying

def f():
  a = A()

f()
# destroying
```

The method is used by Python's `file` object to close the descriptor when you don't need it anymore:

```python
def f():
    a_file = open('a_file.txt')
    ...
```

However, you cannot safely rely on that the destructor (this is how it's called in other languages, like C) will be ever called. For instance, it can be not true in PyPy, MicroPython, or just if the garbage collector is disabled using `gc.disable()`.

The thumb-up rule is to use the destructor only for unimportant things. For example, `aiohttp.ClientSession` uses `__del__` to warn about an unclosed session:

```python
def __del__(self) -> None:
  if not self.closed:
    warnings.warn(
      f"Unclosed client session {self!r}", ResourceWarning
    )
```
