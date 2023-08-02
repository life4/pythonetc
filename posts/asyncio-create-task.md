---
published: 2023-04-18
id: 724
author: orsinium
traces:
  - [module: asyncio, function: create_task]
depends_on:
  - asyncio-run
  - asyncio-sleep
  - asyncio-gather
---

# asyncio.create_task

When talking about asyncio functions, sometimes I used the word "coroutine" and sometimes "task". It's time to tell you the difference:

+ `coroutine` is what async function returns. It can be scheduled, switched, closed, and so on. It's quite similar to generators. In fact, `await` keyword is nothing more than an alias for `yield from`, and `async` is a decorator turning the function from a generator into a coroutine.
+ `asyncio.Future` is like "promise" in JS. It is an object that eventually will hold a coroutine result when it is available. It has `done` method to check if the result is available, `result` to get the result, and so on.
+ `asyncio.Task` is like if coroutine and future had a baby. This is what asyncio mostly works with. It can be scheduled, switched, canceled, and holds its result when ready.

There is a cool function `asyncio.create_task` that can turn a coroutine into a proper task. What's cool about it is that this task immediately gets scheduled. So, if your code later encounters `await`, there is a chance your task will be executed at that point.

```python
import asyncio

async def child():
    print('started child')
    await asyncio.sleep(1)
    print('finished child')

async def main():
    asyncio.create_task(child())
    print('before sleep')
    await asyncio.sleep(0)
    print('after sleep')

asyncio.run(main())
```

Output:

```text
before sleep
started child
after sleep
```

What happened:

1. When `create_task` is called, it is scheduled but not yet executed.
2. When `main` hits `await`, the scheduler switches to `child`.
3. When `child` hits `await`, the scheduler switches to another task, which is `main`
4. When `main` finished, `asyncio.run` returned without waiting for `child` to finish. It's dead in space now.

But what if you want to make sure a scheduled task finishes before exiting? You can pass the task into good old `asyncio.gather`. And later we'll see some ways to wait for it with timeouts or when you don't care about the result.

```python
task = create_task(...)
...
await asyncio.gather(task)
```
