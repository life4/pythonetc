---
published: 2018-04-14
id: 54
author: pushtaev
---

# Parameters unpacking

Python 2 can unpack function parameters if you define them like a tuple:

```ipython {no-run}
In : def between(x, (start, stop)):
...:     return start < x < stop
...:
In : interval = (5, 10)
In : between(2, interval)
Out: False
In : between(7, interval)
Out: True
```

It can even do it recursively:

```ipython {no-run}
In : def determinant_2_x_2(((a,b), (c,d))):
...:     print a*d - c*b
...:

In : determinant_2_x_2([
...:     (1, 2),
...:     (3, 4),
...: ])
-2
```

However, this feature [was removed](https://www.python.org/dev/peps/pep-3113/) in Python 3. You still can do the same by unpacking manually:

```ipython
In : def determinant_2_x_2(matrix):
...:     row1, row2 = matrix
...:     a, b = row1
...:     c, d = row2
...:
...:     return a*d - c*b
...:

In : determinant_2_x_2([
...:     (1, 2),
...:     (3, 4),
...: ])
Out: -2
```
