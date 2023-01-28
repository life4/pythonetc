---
published: 2018-06-02
id: 107
author: pushtaev
---

# async `for` and `with`

Both `for` and `with` can be asynchronous. `async with` uses `__aenter__`  and `__aexit__` magic methods, `async for` uses `__aiter__` and `__anext__`.
All of them are `async` and you can `await` within them:

```python {hide}
import asyncio
async def zero_sleep(t):
    pass
asyncio.sleep = zero_sleep
```

```python {continue} {no-print}
import asyncio

class Sleep:
    def __init__(self, t):
        self._t = t

    async def __aenter__(self):
        await asyncio.sleep(self._t / 2)

    async def __aexit__(self, *args):
        await asyncio.sleep(self._t / 2)

async def main():
    async with Sleep(2):
        print('*')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

When you implement `__iter__` you often don't write an iterator with `__next__` method, you just use `yield`  that makes `__iter__` a generator:

```python {continue} {no-print}
class Bracketed:                  
    def __init__(self, data):     
        self._data = data         
                                  
    def __iter__(self):           
        for x in self._data:      
            yield '({})'.format(x)
                                  
print(list(Bracketed([1, 2, 3]))) 
# ['(1)', '(2)', '(3)']
```

PEP 525 allows you to do the same with `__aiter__`. Both `yield` and `await` in the function body make it *asynchronous generator*. While `await` is used to communicate with the loop, `yield` deals with `for`:

```python {continue} {no-print}
import asyncio                          
                                        
class Slow:                             
    def __init__(self, data, t=1):      
        self._data = data               
        self._t = t                     
                                        
    async def __aiter__(self):          
        for x in self._data:            
            await asyncio.sleep(self._t)
            yield x                     
                                        
async def main():                       
    async for x in Slow([1, 2, 3]):     
        print(x)                        
                                        
loop = asyncio.get_event_loop()         
loop.run_until_complete(main())
```
