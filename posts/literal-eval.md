---
published: 2020-08-25
id: 593
author: orsinium
traces:
  - [{module: ast}, {function: literal_eval}]
---

# ast.literal_eval

`ast.literal_eval` is a restricted version of `eval` that evaluates only literals:

```python
ast.literal_eval('[1, True, "three"]')
# [1, True, 'three']

ast.literal_eval('1+2')
# ValueError: malformed node or string: <_ast.BinOp object ...>
```

This can be used for safely evaluating strings containing Python values from untrusted sources. For example, to support types for environment variables. However, be aware that too large and complex string can crash the interpreter:

```python
>>> import ast
>>> ast.literal_eval('1+1'*1000000)
[1]    32177 segmentation fault  python3
```
