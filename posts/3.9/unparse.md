---
published: 16 June 2020, 18:00
author: orsinium
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
