---
published: 2018-05-10
id: 85
author: pushtaev
---

# How to create a closure

Since loops in Python don't create scopes, you usually need an extra function to create closures. The straightforward way doesn't work:

```python
multipliers = []
for i in range(10):
    multipliers.append(lambda x: x * i)

[multipliers[i](2) for i in range(5)]
# [18, 18, 18, 18, 18]
```

Let's add the extra function:

```python {hide}
multipliers = []
```

```python {continue}
multiplier_creator = lambda i: lambda x: x * i
for i in range(10):
    multipliers.append(multiplier_creator(i))
```

It works this way, but the code can be clumsy, especially if you need `def`, not `lambda`:

```python {hide}
multipliers = []
```

```python {continue}
def multiplier_creator(i):
    def multiplier(x):
        return x * i
    for i in range(10):
        return multiplier

    multipliers.append(multiplier_creator(i))
```

To make it slightly more readable, you can write universal function and get *partials* of it:

```python {hide}
from functools import partial
multipliers = []
```

```python {continue}
multiplier = lambda x, i: x * i
for i in range(10):
    multipliers.append(partial(multiplier, i=i))
```

You can always emulate `partial` with custom `lambda`, but `repr` of partials are generally more readable:

```python
from functools import partial
```

```ipython {continue} {python-interactive-no-check}
In : partial(int, base=2)
Out: functools.partial(<class 'int'>, base=2)

In : lambda x: int(x, base=2)
Out: <function __main__.<lambda>>
```

Fun fact: thanks to the `operator` module this particular example can be expressed even more appealing:

```python
from functools import partial
import operator
multipliers = []
```

```python {continue}
for i in range(10):
    multipliers.append(partial(operator.mul, i))
```
