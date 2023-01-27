---
published: 2018-05-31
id: 105
author: pushtaev
---

# asyncio: schedule a coroutine

Once you write a coroutine, you need three things to get it running: create it, obtain a loop and schedule coroutine's execution.

The first two steps are trivial:

```python {hide}
import asyncio
async def zero_sleep(t):
    pass
asyncio.sleep = zero_sleep
```

```python {continue}
import asyncio
import sys

async def indication(timeout):
    while True:
        print('.', end='')
        sys.stdout.flush()
        await asyncio.sleep(timeout)
```

```python {merge} {continue} {hide}
# suppress "coroutine never awaited" warning
async def coro():
    pass
indication = lambda t: coro
```

```python {merge} {continue}
async def sleep(t, indication_t):    # steps
    coro = indication(indication_t)  # 1
    loop = asyncio.get_event_loop()  # 2

    # ...
    await asyncio.sleep(t)

loop = asyncio.get_event_loop()
loop.run_until_complete(sleep(5, 0.5))
```

The slightly trickier part is to schedule execution of a coroutine within an already running loop.
There are two different ways to achieve that: `loop.create_task(coro)` and `asyncio.ensure_future(coro, loop=loop)`.
Though they both work, they have pretty different semantic.

`create_task` does precisely what we need: it schedules execution of a coroutine and returns a future that allows you to track the coroutine execution (likely by *awaiting* it).
That future is strictly speaking *a task* (`asyncio.Task`), the particular type of futures that wrap a coroutine.

`ensure_future(x)` just *ensures* that `x` is a future or wrap it in one.
If `x` is a coroutine, is uses `create_task` for such wrapping, obviously scheduling `x`.
The previous name for `ensure_future` is `async`; it was changed to respect the fact that `async` is a keyword now.

```python {continue}
import asyncio
import sys

async def indication(timeout):
    while True:
        print('.', end='')
        sys.stdout.flush()
        await asyncio.sleep(timeout)
```

```python {merge} {continue} {hide}
# suppress "coroutine never awaited" warning
async def coro():
    pass
indication = lambda t: coro
```

```python {merge} {continue}
async def sleep(t, indication_t):
    coro = indication(indication_t)
    loop = asyncio.get_event_loop()

    # # Choose one:
    # loop.create_task(coro)
    # asyncio.ensure_future(coro)

    await asyncio.sleep(t)

loop = asyncio.get_event_loop()
loop.run_until_complete(sleep(5, 0.5))
```

Guido [explicitly recommends](https://github.com/python/asyncio/issues/477#issuecomment-268709555) using `create_task()` since its intent is more clear.
