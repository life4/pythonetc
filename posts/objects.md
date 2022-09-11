---
published: 2020-09-15
id: 605
author: orsinium
qname: object
---

# everything is object

Everything is an object, including functions, lambdas, and generators:

```python
g = (i for i in [])
def f(): pass

type(g).__mro__  # (generator, object)
type(f).__mro__  # (function, object)
type(lambda:0).__mro__  # (function, object)
```

Generators have no `__dict__` but functions do!

```python
def count(f):
    def w():
        w.calls += 1
        return f()
    # let's store an attribute in the function!
    w.calls = 0
    return w

@count
def f():
    return 'hello'

f()
f()
f.calls
# 2
```
