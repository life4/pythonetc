---
published: 03 November 2020, 18:00
author: orsinium
---

# comprehensions are functions

As we said, comprehensions compiled into functions. That means, we can take a [types.CodeType](https://docs.python.org/3.8/library/types.html#types.CodeType) object for a comprehension, wrap it into [types.FunctionType](https://docs.python.org/3.8/library/types.html#types.FunctionType), and get a function.

```python
import types

def make():
    [x*2 for x in _]

code = make.__code__.co_consts[1]
func = types.FunctionType(code, globals())

# call the function!
func(iter(range(5)))
# [0, 2, 4, 6, 8]
```
