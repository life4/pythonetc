Let's talk a bit more about scopes.

Any class and function can implicitly use variables from the global scope:

```python
v = 'global'
def f():
  print(f'{v=}')
f()
# v='global'
```

Or from any other enclosing scope, even if it is defined after the fucntion definition:

```python
def f():
  v1 = 'local1'
  def f2():
    def f3():
      print(f'{v1=}')
      print(f'{v2=}')
    v2 = 'local2'
    f3()
  f2()
f()
# v1='local1'
# v2='local2'
```

Class body is a tricky case. It is not considered an enclosing scope for functions defined inside of it:

```python
v = 'global'
class A:
  v = 'local'
  print(f'A {v=}')
  def f():
    print(f'f {v=}')
# A v='local'

A.f()
# f v='global'
```
