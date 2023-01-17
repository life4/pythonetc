---
published: 2018-05-25
id: 99
author: pushtaev
---

# Nested context managers

Sometimes you want to run a code block with multiple context managers:

```python {hide}
from contextlib import contextmanager

@contextmanager
def fake_open(path):
    yield path

open = fake_open
```

```python {continue}
with open('f') as f:
    with open('g') as g:
        with open('h') as h:
            pass
```

Since Python 2.7 and 3.1, you can do it with a single `with` expression:

```python {continue}
o = open
with o('f') as f, o('g') as g, o('h') as h:
    pass
```

Before that, you could you use the `contextlib.nested` function:

```python {continue} {hide}
@contextmanager
def fake_nested(*args):
    yield args
    
# the original one is deprecated
nested = fake_nested
```

```python {continue}
with nested(o('f'), o('g'), o('h')) as (f, g, h):
    pass
```

It still can be used while working with an unknown number of context managers (`nested(*managers)`), but it throws the warning in the modern Python interpreter.

Instead, the more advanced tool is provided. `contextlib.ExitStack` allows you to enter any number of contexts at the arbitrary time but guarantees to exit them at the end:

```python {continue} {hide}
from contextlib import ExitStack
filenames = ['a', 'b', 'c']
```

```python {continue}
with ExitStack() as stack:
    f = stack.enter_context(o('f'))
    g = stack.enter_context(o('g'))
    other = [
        stack.enter_context(o(filename))
        for filename in filenames
    ]
```
