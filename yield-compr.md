Accidentally, `yield` can be used in generator expressions and comprehensions:

```python
[(yield i) for i in 'ab']
# <generator object <listcomp> at 0x7f2ba1431f48>

list([(yield i) for i in 'ab'])
# ['a', 'b']

list((yield i) for i in 'ab')
# ['a', None, 'b', None]
```

This is because `yield` can be used in any function (turning it into a generator) and comprehensions are compiled into functions:

```python
>>> dis.dis("[(yield i) for i in range(3)]")                                                                                                                                             
0 LOAD_CONST     0 (<code object <listcomp> ...>)
2 LOAD_CONST     1 ('<listcomp>')
4 MAKE_FUNCTION  0
...
```

This produces a warning in Python 3.7 and will raise `SyntaxError` in python 3.8+. However, `yield` inside `lambda` still can be used:

```python
a = lambda x: (yield x)
list(a(1))
# [1]
```
