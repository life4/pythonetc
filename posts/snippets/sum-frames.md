---
published: 2020-06-30
author: orsinium
---

# sum implemented on frames

Let's  have more fun with frames and recursion. There is sum function that adds 2 natural small numbers by getting down into recursive calls and then counting back the stack size:

```python
import inspect

def _sum(a, b):
    print(a, b)
    if a != 0:
        return _sum(a-1, b)
    if b != 0:
        return _sum(a, b-1)
    return len(inspect.stack())

  def sum(a, b):
    return _sum(a, b) - len(inspect.stack()) - 1
```
