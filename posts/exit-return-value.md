---
published: 2018-04-24
id: 67
author: pushtaev
---

# `__exit__` return value

Though decorators and context managers are quite similar and often interchangeable, context managers are severely more limited. You can't skip a block or execute it twice; it always runs exactly one time.

However, you can control whether the exception that is raised inside a context should be propagated to the caller or not. It's done by the slightly obscure way: the exception is suppressed if `__exit__` return a true value:

```python {no-print}
class Atomic:
    def __enter__(self):
        print('BEGIN')

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(
                'ROLLBACK due to {}({})'.format(
                    exc_type, exc_value
                )
            )
        else:
            print('COMMIT')

        return True

with Atomic():
    print('A')

with Atomic():
    print('B')
    raise RuntimeError('C')
```

The output is:

```txt
BEGIN
A
COMMIT
BEGIN
B
ROLLBACK due to <type 'exceptions.RuntimeError'>(C)
```
