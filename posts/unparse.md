---
published: 2020-06-16
id: 571
author: orsinium
topic:
  - stdlib
  - function
qname: ast.unparse
python: "3.9"
---

# ast.unparse

Python 3.9 introduces a new function [ast.unparse](https://docs.python.org/3.9/library/ast.html#ast.unparse). It accepts a parsed AST and produces a Python code. This code if parsed will produce the same AST:

```python
import ast
tree = ast.parse('a=(1+2)+3 # example')
ast.unparse(tree)
# '\na = 1 + 2 + 3'
```

It knows nothing about the initial formatting and comments. So, it's not a code formatter but a tool to simplify visual AST analysis. Also, it can be used for code generation.
