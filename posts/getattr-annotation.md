---
published: 2021-03-30
author: orsinium
pep: 526
python: "3.6"
---

# getattr type annotaions (PEP-526)

[PEP-526](https://www.python.org/dev/peps/pep-0526/), introducing syntax for variable annotations (landed in Python 3.6), allows annotating any valid assignment target:

```python
c.x: int = 0
c.y: int

d = {}
d['a']: int = 0
d['b']: int
```

The last line is the most interesting one. Adding annotations to an expression suppresses its execution:

```python
d = {}

# fails
d[1]
# KeyError: 1

# nothing happens
d[1]: 1
```

Despite being a part of the PEP, it's not supported by [mypy](http://mypy-lang.org/):

```bash
$ cat tmp.py
d = {}
d['a']: int
d['b']: str
reveal_type(d['a'])
reveal_type(d['b'])

$ mypy tmp.py
tmp.py:2: error: Unexpected type declaration
tmp.py:3: error: Unexpected type declaration
tmp.py:4: note: Revealed type is 'Any'
tmp.py:5: note: Revealed type is 'Any'
```
