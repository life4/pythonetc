---
author: orsinium
traces:
  - [module: asyncio, function: sleep]
---
# asyncio.sleep

Your best companion in learning asyncio is `asyncio.sleep`. It works like `time.sleep` making the calling code to wait the given number of seconds. This is the simplest example of IO-bound task because while sleeping, your code literally does nothing but waits. And unlike `time.sleep`, `asyncio.sleep` is async. That means, while the calling task waits for it to finish, another task can be executed.

```python
import asyncio
import time

async def main():
    start = time.time()
    await asyncio.sleep(2)
    return int(time.time() - start)

asyncio.run(main())
# 2
```

You can't yet see how the code switches to another task while waiting because we have only one task. But bear with me, in the next posts we'll get to it.
