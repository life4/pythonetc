---
published: 2020-12-29
id: 644
author: orsinium
topic:
  - builtin
  - method
qname: str.join
---

# join strings

What is the fastest way to build a string from many substrings in a loop? In other words, how to concatenate fast when we don't know in advance how many strings we have? There are many discussions about it, and the common advice is that strings are immutable, so it's better to use a list and then `str.join` it. Let's not trust anyone and just check it.

The straightforward solution:

```python
%%timeit
s = ''
for _ in range(10*8):
  s += 'a'
# 4.04 µs ± 256 ns per loop
```

Using lists:

```python
%%timeit
a = []
for _ in range(10*8):
  a.append('a')
''.join(a)
# 4.06 µs ± 144 ns per loop
```

So, it's about the same. But we can go deeper. What about generator expressions?

```python
%%timeit
''.join('a' for _ in range(10*8))
# 3.56 µs ± 95.9 ns per loop
```

A bit faster. What if we use list comprehensions instead?

```python
%%timeit
''.join(['a' for _ in range(10*8)])
# 2.52 µs ± 42.1 ns per loop
```

Wow, this is 1.6x faster than what we had before. Can you make it faster?

And there should be a disclaimer:

1. Avoid [premature optimization](http://wiki.c2.com/?PrematureOptimization), value readability over performance when using a bit slower operation is tolerable.

2. If you think that something is slow, prove it first. It can be different in your case.
