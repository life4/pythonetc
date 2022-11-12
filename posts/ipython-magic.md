---
author: VadimPushtaev
id: 14
published: 2018-03-20
sequence: ipython-magic
---

# iPython magic

iPython supports a number of magic commands that can make your life easier.
There are two types of them: line magics and cell magics.
Line magics start with `%` sign, `%timeit` is a good example:

```ipython {no-run}
In [1]: %timeit sum(x**2 for x in range(1000))
243 µs ± 2.31 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

Cell magics start with double `%` sign, look at `%%ruby`:

```ipython
In [2]: %%ruby
   ...: 3.times do |x|
   ...:   puts x
   ...: end
   ...:
0
1
2
```

You can even define custom magics.
This is an example magic that helps you ignore an expression result
except the very end:

```ipython
In [3]: from IPython.core.magic import register_line_magic

In [4]: @register_line_magic
   ...: def tail(line):
   ...:     result = repr(eval(line))
   ...:     if len(result) > 100:
   ...:         return '... {}'.format(result[-100:])
   ...:

In [5]: %tail list(range(1000))
Out[5]: '...  980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]'
```

All that is also true for Jupyter Notebook.
