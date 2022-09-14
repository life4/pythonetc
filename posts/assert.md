---
published: 2020-07-30
id: 585
author: orsinium
topics:
  - keyword
qname: assert
---

# assert

Basically, `assert` could be a function:

```python

def assert_(test, *args):
    if not test:
        raise AssertionError(*args)

assert_(2 + 2 == 4, 'the world is broken')
```

However, there are few advantages of assert as directive over assert as a function:

1. All asserts removed on the bytecode compilation step if [optimization is enabled](https://t.me/pythonetc/115).

2. The message is lazy and executed only when needed:

```python
assert False, print("executed")
# executed
# AssertionError: None

assert True, print("not executed")
# (prints nothing)
```
