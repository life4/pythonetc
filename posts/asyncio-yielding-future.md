---
published: 2018-05-28
id: 102
author: pushtaev
---

# asyncio: yielding future

Once an `asyncio` coroutine wants to stop and communicate with the event loop, it uses `await obj` (or `yield from obj` before Python 3.6).
An `obj` should be another coroutine, `asyncio.Future` or any custom Future-like object (any object with the `__await__` method defined).

```python {hide}
import asyncio
orig_future = asyncio.Future
class FakeFuture:
    def __await__(self):
        yield
            
asyncio.Future = FakeFuture  # the following code is going to lock forever otherwise
```

```python {continue}
async def coroutine():
    await another_coroutine()

async def another_coroutine():
    future = asyncio.Future()
    await future

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine())
```

```python {hide} {continue}
asyncio.Future = orig_future
```

Once the coroutine awaits another one, the second starts to run instead of the first. If it awaits the third one, the third one runs.
It goes on and on until some coroutine awaits a future. The future actually *yields* the value, so the loop finally gains control.

What value does the future yield? It yields itself. Can you yield a future directly? No, it's an internal detail you shouldn't normally worry about.

```python {continue} {shield:RuntimeError}
class Awaitable:
    def __await__(self):
        future = asyncio.Future()
        yield future
            # RuntimeError: yield was used
            # instead of yield from in task

async def coroutine():
    await Awaitable()

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine())
```

Why does this error occur? How does `asyncio` know it's you who yield the future, not the future itself
There is a simple protection: the future [raises the internal flag](https://github.com/python/cpython/blob/22feeb88b473b288950cdb2f6c5d28692274b5f9/Lib/asyncio/futures.py#L259) before yielding.
