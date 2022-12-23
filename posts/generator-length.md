---
published: 2018-04-17
id: 58
author: pushtaev
---

# Generator length

Sometimes you need to know the size of a generator without retrieving the actual values. Some generators support `len()`, but this is not the rule:

```ipython {shield:TypeError}
In : len(range(10000))
Out: 10000

In : gen = (x ** 2 for x in range(10000))
In : len(gen)
...
TypeError: object of type 'generator' has no len()
```

The straightforward solution is to use an intermediate list:

```ipython {continue}
In : len(list(gen))
Out: 10000
```

Though fully functional, this solution requires enough memory to store all the yielded values. The simple idiom allows to avoid such a waste:

```python {hide}
# Reset generator
gen = (x ** 2 for x in range(10000))
```

```ipython {continue}
In : sum(1 for _ in gen)
Out: 10000
```
