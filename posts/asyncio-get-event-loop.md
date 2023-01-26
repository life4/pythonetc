---
published: 2018-05-30
id: 104
author: pushtaev
---

# asyncio: `get_event_loop`

In `asyncio`, the main thread loop is automatically created for you once you call `asyncio.get_event_loop()`. That doesn't happen in any other thread:

```ipython {no-run}
In : asyncio.get_event_loop()
Out: <_UnixSelectorEventLoop running=False closed=False debug=False>

In : Thread(target=asyncio.get_event_loop).start()
Exception in thread Thread-385:
RuntimeError: There is no current event loop in thread 'Thread-385'.
```

The `get_event_loop()` method returns the loop bound to the current thread.
You can use `set_event_loop(loop)` to bind the `loop` to the current thread after creating it with `loop = asyncio.new_event_loop()`.

You can run any loop, even if another one is bound to the thread.
That's why in Python 3.6 `get_event_loop()` works differently within a coroutine.
It returns not the loop bound to the thread, but the currently running loop. It's important when a coroutine tries to interact with *its* loop:

```python
import asyncio
async def zero_sleep(t):
    pass
asyncio.sleep = zero_sleep
```

```python {continue}
import asyncio
import sys

async def sleep(t, indication_t):
    async def indication():
        while True:
            print('.', end='')
            sys.stdout.flush()
            await asyncio.sleep(indication_t)

    loop = asyncio.get_event_loop()  # <-- here
    task = loop.create_task(indication())
    await asyncio.sleep(t)
    task.cancel()

loop = asyncio.get_event_loop()
loop.run_until_complete(sleep(5, 0.5))
```

Even though you can run any loop you can never run two loops in the single thread. Though it's technically possible, it's explicitly forbidden by `asyncio`:

```ipython {continue} {shield:RuntimeError}
In : async def run_another():
...:     loop = asyncio.new_event_loop()
...:     loop.run_forever()
In : loop = asyncio.get_event_loop()
In : loop.run_until_complete(run_another())
RuntimeError: Cannot run the event loop while another loop is running
```
