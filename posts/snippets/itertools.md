---
published: 2020-09-03
author: orsinium
---

# itertools

Some functional languages, like Elixir, have in the standard library a huge collection of functions to work with lazy enumerables (in Python, we name them [iterators](https://articles.orsinium.dev/python/iterators/)). In Python, this role is on [itertools](https://docs.python.org/3/library/itertools.html). However, `itertools` is a relatively small collection of such functions, it contains only most important and basic ones (maybe, a bit of junk, but so). The documentation has [Itertools Recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes) with some useful functions. A few examples:

```python
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def prepend(value, iterator):
    "Prepend a single value in front of an iterator"
    # prepend(1, [2, 3, 4]) -> 1 2 3 4
    return chain([value], iterator)

def tail(n, iterable):
    "Return an iterator over the last n items"
    # tail(3, 'ABCDEFG') --> E F G
    return iter(collections.deque(iterable, maxlen=n))

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)
```

All these examples and much more can be imported from [more-itertools](https://github.com/more-itertools/more-itertools) third-party library.
