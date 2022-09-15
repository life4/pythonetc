---
published: 2022-09-06
id: 696
author: orsinium
traces:
  - [{module: gc}, {function: is_finalized}]
python: "3.9"
---

# gc.is_finalized

By using `__del__` and global variables, it is possible to leave a reference to the object after it was "destroyed":

```python
runner = None
class Lazarus:
  def __del__(self):
    print('destroying')
    global runner
    runner = self

lazarus = Lazarus()
print(lazarus)
# <__main__.Lazarus object at 0x7f853df0a790>
del lazarus
# destroying
print(runner)
# <__main__.Lazarus object at 0x7f853df0a790>
```

In the example above, `runner` points to the same object as `lazarus` did and it's not destroyed. If you remove this reference, the object will stay in the memory forever because it's not tracked by the garbage collector anymore:

```python
del runner  # it will NOT produce "destroying" message
```

This can lead to a strange situation when you have an object that escapes the tracking and will be never collected.

In Python 3.9, the function [gc.is_finalized](https://docs.python.org/3/library/gc.html#gc.is_finalized) was introduced that tells you if the given object is a such runner:

```python
import gc
lazarus = Lazarus()
gc.is_finalized(lazarus) # False
del lazarus
gc.is_finalized(runner)  # True
```

It's hard to imagine a situation when you'll need it, though. The main conclusion you can make out of it is that you can break things with a destructor, so don't overuse it.
