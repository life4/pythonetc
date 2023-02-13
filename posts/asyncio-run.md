---
published: 2023-03-28
author: orsinium
traces:
  - [module: asyncio, function: run]
depends_on:
  - asyncio
---

# asyncio.run

Async is like mold in your fridge or GPU license in your dependencies. It propagates through your code, taking over every corner of it. You can call sync functions from async functions but async functions can be called only from other async functions, using the `await` keyword.

This one returns a coroutine instead of a result:

```python
async def welcome():
    return 'hello world'

def main():
    return welcome()

main()
# <coroutine object welcome at 0x...>
```

This is how `main` should look instead:

```python
async def main():
    result = await welcome()
    return result
```

Alright, but how to call the root function? It also returns a coroutine! The answer is `asyncio.run`, which will take a coroutine, schedule it, and return its result:

```python
coro = main()
result = asyncio.run(coro)
print(result)
```

Keep in mind that `asyncio.run` should be called only once. You can't use it to call an async function from any sync function. Again, if you have an async function to call, all functions calling it (and all functions calling them, and so on) should also be async. Like a mold.
