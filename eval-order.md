Python uses [eager evaluation](https://en.wikipedia.org/wiki/Eager_evaluation). When a function is called, all its arguments are evaluated from left to right and only then their results are passed into the function:

```python
print(print(1) or 2, print(3) or 4)
# 1
# 3
# 2 4
```

Operators `and` and `or` are lazy, the right value is evaluated only if needed (for `or` if the left value is falsy, and for `and` if the left value is truthy):

```python
print(1) or print(2) and print(3)
# 1
# 2
```

For mathematical operators, the precedence is how it is in math:

```python
1 + 2 * 3
# 7
```

The most interesting case is operator `**` (power) which is (supposedly, the only thing in Python which is) evaluated from right to left:

```python
2 ** 3 ** 4 == 2 ** (3 ** 4)
# True
```
