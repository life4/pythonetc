---
published: 2022-07-26
id: 690
author: orsinium
qname: typing.TYPE_CHECKING
---

# typing.TYPE_CHECKING

Often, your type annotations will have circular dependencies. For example, `Article` has an attribute `category: Category`, and `Category` has attribute `articles: list[Article]`. If both classes are in the same file, adding `from __future__ import annotations` would solve the issue. But what if they are in different modules? Then you can hide imports that you need only for type annotations inside of the [if TYPE_CHECKING](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING) block:

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .category import Category

@dataclass
class Article:
  category: Category
```

Fun fact: this constant is defined as `TYPE_CHECKING = False`. It won't be executed at runtime, but the type checker is a static analyzer, it doesn't care.
