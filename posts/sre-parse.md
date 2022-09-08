---
published: 7 September 2021, 18:00
author: orsinium
---

# sre_parse

Internally, the module [re](https://docs.python.org/3/library/re.html) uses 2 undocumented libraries:

+ `sre_parse` to parse regular expressions into an abstract syntax tree.
+ `sre_compile` to compile parsed expression.

The first one can be used to see how a regexp was parsed by Python. There are many better tools and services (like [regex101.com](https://regex101.com/)) to debug regular expressions but this one is already in the stdlib.

```python
>>> import sre_parse
>>> sre_parse.parse(r'([Pp]ython)\s?etc').dump()
SUBPATTERN 1 0 0
  IN
    LITERAL 80
    LITERAL 112
  LITERAL 121
  LITERAL 116
  LITERAL 104
  LITERAL 111
  LITERAL 110
MAX_REPEAT 0 1
  IN
    CATEGORY CATEGORY_SPACE
LITERAL 101
LITERAL 116
LITERAL 99
```
