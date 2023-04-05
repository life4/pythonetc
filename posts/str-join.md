---
author: orsinium
traces:
  - [type: str, method: join]
---

# str.join

The `str.join` method is used to join a list of strings together using the given delimiter:

```python
'..'.join(['hello', '@pythonetc'])
# 'hello..@pythonetc'
```

Many newcomers are confused by this syntax. Why `join` is a method of `str`? Why not a function? Why not a method of `list`?

The first question is quite easy to answer: it's not a function to keep the built-in namespace clean. Also, the delimiter can be only `str`. The built-in functions are mostly the ones that can accept arguments of multiple types. For example, the argument `len` can be str, list, tuple, and any other collection. Exceptions, like `chr`, are caused by limitations of the parser: `1.ord()` is a SyntaxError, and `(1).ord()` doesn't look nice.

On the second question: it's not a method of `list` because it supports any iterable, not only lists. For example:

```python
def f():
    yield 'hello'
    yield '@pythonetc'

' '.join(f())
# 'hello @pythonetc'
```

If you know someone who starts learning Python, tell them: there are no stupid questions. It's great to question some ideas and decisions. Learning about the motivation behind them helps to better understand the language. The `join` is a method of `str` not "just because", and it's great to know why.
