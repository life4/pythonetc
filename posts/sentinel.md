---
published: 2020-10-20
author: orsinium
qname: unittest.mock.sentinel
---

# unittest.mock.sentinel

Some functions can accept as an argument value of any type or no value at all. If you set the default value to `None` you can't say if `None` was explicitly passed or not. For example, the [default value](https://docs.python.org/3/library/argparse.html#default) for [argparse.ArgumentParser.add_argument](https://docs.python.org/3/library/argparse.html#the-add-argument-method). For this purpose, you can create a new object and then use `is` check:

```python
DEFAULT = object()

def f(arg=DEFAULT):
  if arg is DEFAULT:
      return 'no value passed'
  return f'passed {arg}'

f()     # 'no value passed'
f(None) # 'passed None'
f(1)    # 'passed 1'
f(object()) # 'passed <object object at ...>'
```

The module `unittest.mock` provides a [sentinel](https://docs.python.org/3/library/unittest.mock.html#sentinel) registry to create unique (by name) objects for the testing purpose:

```python
sentinel.ab.name # 'ab'
sentinel.ab is sentinel.ab  # True
sentinel.ab is sentinel.cd  # False
```
