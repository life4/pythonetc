---
published: 2021-03-04
id: 650
author: orsinium
qname: str
---

# int to str performance

Let's learn a bit more about strings performance. What if instead of an unknown amount of strings we have only a few known variables?

```python
s1 = 'hello, '
s2 = '@pythonetc'

%timeit s1+s2
# 56.7 ns ± 6.17 ns per loop

%timeit ''.join([s1, s2])
# 110 ns ± 6.09 ns per loop

%timeit '{}{}'.format(s1, s2)
# 63.3 ns ± 6.69 ns per loop

%timeit f'{s1}{s2}'
# 57 ns ± 5.43 ns per loop
```

No surprises here, `+` and f-strings are equally good, `str.format` is quite close. But what if we have numbers instead?

```python
n1 = 123
n2 = 456
%timeit str(n1)+str(n2)
# 374 ns ± 7.09 ns per loop

%timeit '{}{}'.format(n1, n2)
# 249 ns ± 4.73 ns per loop

%timeit f'{n1}{n2}'
# 208 ns ± 3.49 ns per loop
```

In this case, formatting is faster because it doesn't create intermediate strings. However, there is something else about f-strings. Let's measure how long it takes just to convert an `int` into an `str`:

```python
%timeit str(n1)
# 138 ns ± 4.86 ns per loop

%timeit '{}'.format(n1)
# 148 ns ± 3.49 ns per loop

%timeit format(n1, '')
# 91.8 ns ± 6.12 ns per loop

%timeit f'{n1}'
# 63.8 ns ± 6.13 ns per loop
```

Wow, f-strings are twice faster than just `str`! This is because f-strings are part of the grammar but `str` is just a function that requires function-lookup machinery:

```python
import dis
dis.dis("f'{n1}'")
  1           0 LOAD_NAME                0 (n1)
              2 FORMAT_VALUE             0
              4 RETURN_VALUE

dis.dis("str(n1)")
  1           0 LOAD_NAME                0 (str)
              2 LOAD_NAME                1 (n1)
              4 CALL_FUNCTION            1
              6 RETURN_VALUE
```

And once more, disclaimer: readability is more important than performance until proven otherwise. Use your knowledge with caution :)
