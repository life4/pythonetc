---
published: 2023-04-25
author: orsinium
traces:
  - [module: asyncio, class: Task]
depends_on:
  - asyncio-create-task
---

# asyncio.Task may be GCed

In the previous post, we had the following code:

```python
import asyncio

async def child():
  ...

async def main():
    asyncio.create_task(child())
    ...

asyncio.run(main())
```

Can you spot a bug?

Since we don't store a reference to the background task we create, the garbage collector may destroy the task before it finishes. To avoid that, we need to store a reference to the task until it finishes. The official documentation recommends the following pattern:

```python
bg_tasks = set()

async def main():
    t = asyncio.create_task(child())
    # hold the reference to the task
    # in a global set
    bg_tasks.add(t)
    # automatically remove the task
    # from the set when it's done
    t.add_done_callback(t.discard)
    ...
```
