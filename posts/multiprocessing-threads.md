---
published: 2018-04-22
id: 64
author: pushtaev
---

# multiprocessing threads

Python `multiprocessing` module allows you to spawn not only processes but threads as well. Mind, however, than CPython is notorious for its GIL (global interpreter lock), the interpreter feature that doesn't allow different threads run Python bytecode simultaneously.

That means that threads are only useful when your program spends time outside of Python interpreter, usually waiting for IO. For example, downloading three different Wikipedia articles at once with threads will be as efficient as with processes (and thrice as efficient as downloading using only one process):

```python {no-run}
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

def download_wiki_article(article):
    url = 'http://de.wikipedia.org/wiki/'
    return requests.get(url + article)

process_pool = Pool(3)
thread_pool = ThreadPool(3)

thread_pool.map(download_wiki_article, ['a', 'b', 'c'])
# 376 ms ± 11 ms

process_pool.map(download_wiki_article, ['a', 'b', 'c'])
# 373 ms ± 3.17 ms

[download_wiki_article(a) for a in ['a', 'b', 'c']]
# 1.09 s ± 27.9 ms
```

On the other hand, it doesn't make much sense to solve CPU-heavy tasks with threads:

```python {no-run}
import math
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

def f(x):
    return math.factorial(x)

process_pool = Pool(4)
thread_pool = ThreadPool(4)
inputs = [i ** 2 for i in range(100, 130)]

[f(x) for x in inputs]
# 1.48 s ± 7.61 ms

thread_pool.map(f, inputs)
# 1.48 s ± 7.78 ms

process_pool.map(f, inputs)
# 478 ms ± 7.55 ms
```
