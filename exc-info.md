When something fails, usually you want to log it. Let's have a look at a small toy example:

```python
from logging import getLogger

logger = getLogger(__name__)
channels = dict(
  pythonetc='Python etc',
)

def update_channel(slug, name):
  try:
    old_name = channels[slug]
  except KeyError as exc:
    logger.error(repr(exc))
    channels[slug] = name
    return
  if name != old_name:
    channels[slug] = name

update_channel('telegram', 'Telegram News')
# Logged: KeyError('telegram')
```

This example has a few issues:

+ There is no explicit log message. So, when it fails, you can't search in the project where this log record comes from.
+ There is no traceback. When the `try` block execution is more complicated, we want to be able to track where exactly an the call stack the exception occured. To achieve it, logger methods provide `exc_info` argument. When it is set to `True`, the current exception with traceback will be added into the log message.

So, this is how we can do it better:

```python
def update_channel(slug, name):
  try:
    old_name = channels[slug]
  except KeyError as exc:
    logger.error('channel not found', exc_info=True)
  ...

update_channel('telegram', 'Telegram News')
# channel not found
# Traceback (most recent call last):
#   File "...", line 10, in update_channel
#     old_name = channels[slug]
# KeyError: 'telegram'
```

Also, logger provides a convenient method `exception` which is the same as `error` with `exc_info=True`:

```python
logger.exception('channel not found')
```
