---
author: orsinium
traces:
  - [{type: str}, {method: split}]
---

# str.split

The `str.split` method splits the string by the given delimeter:

```python
'-1-2--3--'.split('-')
# ['', '1', '2', '', '3', '', '']
```

What's interesting, it will behave very differently if you don't pass the delimeter:

1. The string will be split by all whitespace characters: new line, space, tab, etc.
2. Repeated whitespaces will be treated as one.
3. The whitespaces from the beginning and the end of the string will be ignored.

```python
' a b  c\t\nd   '.split()
```

It's very useful for splitting a string by words. Or for removing all whitespace noise:

```python
msg = 'hello  @pythonetc! \n'
' '.join(msg.split())
# 'hello @pythonetc!'
```
