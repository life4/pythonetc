---
published: 2018-05-23
id: 98
author: pushtaev
---

# asyncio: futures

While using `asyncio`, you rarely need to mess with futures directly, they are usually concealed and are dealt by the loop itself.

However, custom futures might be a mighty tool.
[This example](https://repl.it/@VadimPushtaev/aiosqr) demonstrates how a coroutine can be stopped for batch processing.
The `sqr` coroutine creates and awaits future that can be processed not by the loop,
but by the custom `Queue`, that sends HTTP requests once every second, not immediately on demand.
