---
published: 2023-03-21
author: orsinium
traces:
  - [module: asyncio]
---

# asyncio

It's time for us to talk about async/await in Python. That's a big and difficult topic but a very important one if you're working with the network.

Everything your program does belongs to one of the two classes:

+ **CPU-bound tasks**. This is when you do a lot of computations, and the fan of your PC makes helicopter noises. You can speed up computations with multiprocessing, which is a pain in the ass to do correctly.
+ **IO-bound tasks**. This is when your code does nothing except wait for a response from the outside world. It includes making all kinds of network requests (sending logs, querying a database, crawling a website), network responses (like when you have a web app), and working with files. You can speed up it using async/await syntax.

The basics are quite simple:

1. If you define a function using `async def` instead of just `def`, it will return a "coroutine" when is called instead of immediately running and calculating the result.
2. If you call inside an async function another async function with adding `await` before it, Python will request execution of this coroutine, switch to something else, and return the result when it is available.
3. The module asyncio contains some functions to work with async code and the scheduler that decides when to run which task.

This is a very basic overview. You can read the official asyncio documentation to learn more. In follow-up posts, we will cover most of asyncio functions, one by one.
