---
author: orsinium
traces:
  - [module: asyncio, function: gather]
depends_on:
  - asyncio-run
  - asyncio-sleep
---

# asyncio.gather

The `asyncio.gather` is the function that you will use the most. You pass in it multiple coroutines, it schedules them, waits for all to finish, and returns the list of results in the same order.

```python
import asyncio

URLS = ['google.com', 'github.com', 't.me']

async def check_alive(url):
    print(f'started {url}')
    i = URLS.index(url)
    await asyncio.sleep(3 - i)
    print(f'finished {url}')
    return i

async def main():
    coros = [check_alive(url) for url in URLS]
    statuses = await asyncio.gather(*coros)
    for url, alive in zip(URLS, statuses):
        print(url, alive)

asyncio.run(main())
```

Output:

```plain
started google.com
started github.com
started t.me
finished t.me
finished github.com
finished google.com
google.com 0
github.com 1
t.me 2
```

That's what happened:

1. `asyncio.gather` schedules all tasks in order as they are passed.
2. We made the first task wait 3 seconds, the second wait 2 second, and the last one wait 1 second. And the tasks finished as soon as they could, without making everyone to wait for the first task.
3. `asyncio.gather` waits for all tasks to finish.
4. `asyncio.gather` returns list of results in the order as the coroutines were passed in it. So, it's safe to `zip` results with input values.
