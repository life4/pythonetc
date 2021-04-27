# textwrap.dedent

Published: 27 April 2021, 18:00

Multiline string literal preserves every symbol between opening and closing quotes, including indentation:

```python
def f():
  return """
    hello
      world
  """
f()
# '\n    hello\n      world\n  '
```

A possible solution is to remove indentation, Python will still correctly parse the code:

```python
def f():
  return """
hello
  world
"""
f()
# '\nhello\n  world\n'
```

However, it's difficult to read because it looks like the literal is outside of the function body but it's not. So, a much better solution is not to break the indentation but instead remove it from the string content using [textwrap.dedent](https://docs.python.org/3/library/textwrap.html#textwrap.dedent):

```python
from textwrap import dedent

def f():
  return dedent("""
    hello
      world
  """)
f()
# '\nhello\n  world\n'
```
