---
published: 2018-04-06
id: 39
author: pushtaev
---

# __getitem__ and slices

In Python, you can override square brackets operator (`[]`) by defining `__getitem__` magic method.
The example is `Cycle` object that virtually contains an infinite number of repeated elements:

```python {no-print}
class Cycle:
    def __init__(self, lst):
        self._lst = lst

    def __getitem__(self, index):
        return self._lst[index % len(self._lst)]

print(Cycle(['a', 'b', 'c'])[100])  # prints 'b'
```

The unusual thing here is `[]` operator supports a unique syntax.
It can be used not only like this — `[2]`, but also like this — `[2:10]`,
or `[2:10:2]`, or `[2::2]`, or even `[:]`.
The semantic is `[start:stop:step]`
but you can use it any way you want for your custom objects.

But what `__getitem__` gets as an `index` parameter if you call it using that syntax?
The [slice objects](https://docs.python.org/3/library/functions.html#slice) exist precisely for this case.

```ipython {no-print}
In : class Inspector:
...:     def __getitem__(self, index):
...:         print(index)
...:
In : Inspector()[1]
1
In : Inspector()[1:2]
slice(1, 2, None)
In : Inspector()[1:2:3]
slice(1, 2, 3)
In : Inspector()[:]
slice(None, None, None)
```

You can even combine tuple and slice syntaxes:

```ipython {continue} {no-print}
In : Inspector()[:, 0, :]
(slice(None, None, None), 0, slice(None, None, None))
```

`slice` is not doing anything for you except simply storing `start`, `stop` and `step` attributes.

```ipython
In : s = slice(1, 2, 3)
In : s.start
Out: 1
In : s.stop
Out: 2
In : s.step
Out: 3
```
