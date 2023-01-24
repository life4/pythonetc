---
published: 2018-05-29
id: 103
author: pushtaev
---

# asyncio: await in `__await__`

Objects with the `__await__` method defined are called *Future-like*. `__await__` is meant to *yield* a value to the loop (`asyncio.Future` does exactly this).

However, you may want to *await* inside `__await__`. The problem is, `__await__` is not `async`, so `await` is a syntax error:

```python {no-run}
class Future:
    def __await__(self):
        await asyncio.sleep(1)

#     await asyncio.sleep(1)
#                 ^
# SyntaxError: invalid syntax
```

You can use `yield from` instead:

```python {hide}
import asyncio
loop = asyncio.get_event_loop()
```

```python {continue}
class Future:
    def __await__(self):
        yield from asyncio.sleep(1)
```

Another problem is, you can only *yield from* native coroutine in another coroutine (whether native or generator-based). `__await__` is neither though:

```python {continue}
async def sleep_one_sec():
    await asyncio.sleep(1)
```

```python {continue} {hide}
# We need to suppress `coroutine 'sleep_one_sec' was never awaited` warning
async def fake_sleep_one_sec():
    await asyncio.sleep(0)
coro = fake_sleep_one_sec()
sleep_one_sec = lambda: coro     
```

```python {continue} {shield:TypeError} {merge}
class Future:
    def __await__(self):
        yield from sleep_one_sec()

loop.run_until_complete(Future())

#      1 class Future:
#      2     def __await__(self):
#----> 3         yield from sleep_one_sec()
#      4
# TypeError: cannot 'yield from' a coroutine object
# in a non-coroutine generator
```

```python {hide} {continue}
loop.run_until_complete(coro)  # to suppress the warning
```

One of the solutions would be to call `__await__` manually:

```python {continue}
class Future:
    def __await__(self):
        yield from sleep_one_sec().__await__()
```

Another one is to use generator-based coroutine as an adapter:

```python {continue}
@asyncio.coroutine
def adapter(coroutine):
    yield from coroutine

class Future:
    def __await__(self):
        yield from adapter(sleep_one_sec())
```
