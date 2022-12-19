---
published: 2018-04-15
id: 55
author: pushtaev
---

# Why numbering should start at zero

In Python, `range()` defines all integers in a half-open interval. So `range(2, 10)` means, speaking mathematically, `[2, 10)`. Or, speaking Python, `[2, 3, 4, 5, 6, 7, 8, 9]`.

Despite asymmetry, that is not a mistake nor an accident. It makes perfect sense since it allows you to glue together two adjacent intervals without risk of one-off errors:

```txt
[a, c) = [a, b) + [b, c) 
```

Compare to closed intervals that feel more “natural”:

```txt
[a, c] = [a, b] + [b+1, c]
```

This is also a reason for indexing to start from zero: range(0, N) has exactly `N` elements.

Dijkstra wrote an excellent [article](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html) on the subject back in 1982.
