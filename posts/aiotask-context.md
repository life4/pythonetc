---
published: 2018-06-01
id: 106
author: pushtaev
---

# aiotask-context: contextvars for asyncio

If you want to pass some information down the call chain, you usually use the most straightforward way possible: you pass it as functions arguments.

However, in some cases, it may be highly inconvenient to modify all functions in the chain to propagate some new piece of data.
Instead, you may want to set up some kind of *context* to be used by all functions down the chain. How can this context be technically done?

The simplest solution is a global variable.
In Python, you may also use modules and classes as context holders since they, strictly speaking, are global variables too.
You probably do it on a daily basis for things like loggers.

If your application is multi-threaded, a bare global variable won't work for you since they are not *thread-safe*.
You may have more than one call chain running at the same time, and each of them needs its own context.
The `threading` module gets you covered, it provides the `threading.local()` object that *is* thread-safe.
Store there any data by simply accessing attributes: `threading.local().symbol = '@'`.

Still, both of that approaches are *concurrency-unsafe* meaning they won't work for coroutine call-chain where functions are not only *called* but can be *awaited* too.
Once a coroutine does `await`, an event loop may run a completely different coroutine from a completely different chain. That won't work:

```python {hide}
import asyncio
async def zero_sleep(t):
    pass
asyncio.sleep = zero_sleep
```

```python {continue}
import asyncio
import sys

global_symbol = '.'

async def indication(timeout):
    while True:
        print(global_symbol, end='')
        sys.stdout.flush()
        await asyncio.sleep(timeout)

async def sleep(t, indication_t, symbol='.'):
    loop = asyncio.get_event_loop()

    global global_symbol
    global_symbol = symbol
    task = loop.create_task(indication(indication_t))
    await asyncio.sleep(t)
    task.cancel()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    sleep(1, 0.1, '0'),
    sleep(1, 0.1, 'a'),
    sleep(1, 0.1, 'b'),
    sleep(1, 0.1, 'c'),
))
```

You can fix that by having the loop set and restore the context every time it resumes some coroutine.
The `aiotask_context` module does exactly this by changing the way how tasks are created with `loop.set_task_factory`. This works:

```python {continue}
import asyncio                                
import sys                                    
import aiotask_context as context             
                                              
async def indication(timeout):                
    while True:                               
        print(context.get('symbol'), end='')  
        sys.stdout.flush()                    
        await asyncio.sleep(timeout)          
                                              
async def sleep(t, indication_t, symbol='.'): 
    loop = asyncio.get_event_loop()           
                                              
    context.set(key='symbol', value=symbol)   
    task = loop.create_task(indication(indication_t))
    await asyncio.sleep(t)
    task.cancel()                    
                                              
loop = asyncio.get_event_loop()               
loop.set_task_factory(context.task_factory)   
loop.run_until_complete(asyncio.gather(       
    sleep(1, 0.1, '0'),                       
    sleep(1, 0.1, 'a'),                       
    sleep(1, 0.1, 'b'),                       
    sleep(1, 0.1, 'c'),                       
))
```
