Docstring is a string that goes before all other statements in the function body (comments are ignored):

```python
def f(): 'a'
f.__doc__  # 'a'

def f(): r'a'
f.__doc__  # 'a'
```

It must be a static unicode string. F-strings, byte-strings, variables, or methods can't be used:

```python
def f(): b'a'
f.__doc__  # None

def f(): f'a'
f.__doc__  # None

a = 'a'
def f(): a
f.__doc__  # None

def f(): '{}'.format('a')
f.__doc__  # None
```

Of course, you can just set `__doc__` attribute:

```python
def f(): pass
f.__doc__ = f'{"A!"}'
f.__doc__ # 'A!'
```
