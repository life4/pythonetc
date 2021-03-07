Suppose, you have 10 lists:

```python
lists = [list(range(10_000)) for _ in range(10)]
```

What's the fastest way to join them into one? To have a baseline, let's just `+` everything together:

```python
s = lists
%timeit s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9]
# 1.65 ms ± 25.1 µs per loop
```

Now, let's try to use [functools.reduce](https://t.me/pythonetc/357). It should be about the same but cleaner and doesn't require to know in advance how many lists we have:

```python
from functools import reduce
from operator import add
%timeit reduce(add, lists)
# 1.65 ms ± 27.2 µs per loop
```

Good, about the same speed. However, reduce is not "pythonic" anymore, this is why it was moved from built-ins into `functools`. The more beautiful way to do it is using `sum`:

```python
%timeit sum(lists, start=[])
# 1.64 ms ± 83.8 µs per loop
```

Short and simple. Now, can we make it faster? What if we [itertools.chain](https://t.me/pythonetc/461) everything together?

```python
from itertools import chain
%timeit list(chain(*lists))
# 599 µs ± 20.4 µs per loop
```

Wow, this is about 3 times faster. Can we do better? Let's try something more straightforward:

```python
%%timeit
r = []
for lst in lists:
  r.extend(lst)
# 250 µs ± 5.96 µs per loop
```

Turned out, the most straightforward and simple solution is the fastest one.
