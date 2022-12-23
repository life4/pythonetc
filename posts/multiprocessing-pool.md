---
published: 2018-04-21
id: 62
author: pushtaev
---

# multiprocessing.Pool

If you have a CPU-heavy task and want to utilize all the cores you have, then `multiprocessing.Pool` is for you.
It spawns multiple processes and delegates tasks to them automatically. Simply create a pool with `Pool(number_of_processes)` and run `p.map` with the list of inputs.

```ipython {no-run}
In : import math
In : from multiprocessing import Pool
In : inputs = [i ** 2 for i in range(100, 130)]
In : def f(x):
...:     return len(str(math.factorial(x)))
...:
In : %timeit [f(x) for x in inputs]
1.44 s ± 19.2 ms per loop (...)
In : p = Pool(4)
In : %timeit p.map(f, inputs)
451 ms ± 34 ms per loop (...)
```
