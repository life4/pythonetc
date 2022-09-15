---
published: 2021-04-22
id: 664
author: orsinium
traces:
  - [{module: logging}]
---

# logging extra

Let's have a look at the following log message:

```python
import logging
logger = logging.getLogger(__name__)
logger.warning('user not found')
# user not found
```

When this message is logged, it can be hard based on it alone to reproduce the given situation, to understand what went wrong. So, it's good to provide some additional context. For example:

```python
user_id = 13
logger.warning(f'user #{user_id} not found')
```

That's better, now we know what user it was. However, it's hard to work with such kinds of messages. For example, we want to get a notification when the same type of error messages occurred too many times in a minute. Before, it was one error message, "user not found". Now, for every user, we get a different message. Or another example, if we want to get all messages related to the same user. If we just search for "13", we will get many false positives where "13" means something else, not `user_id`.

The solution is to use [structured logging](softwareengineering.stackexchange.com/questions/312197/). The idea of structured logging is to store all additional values as separate fields instead of mixing everything in one text message. In Python, it can be achieved by passing the variables as the `extra` argument. Most of the logging libraries will recognize and store everything passed into `extra`. For example, how it looks like in [python-json-logger](https://pypi.org/project/python-json-logger/):

```python
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.warning('user not found', extra=dict(user_id=13))
# {"message": "user not found", "user_id": 13}
```

However, the default formatter doesn't show `extra`:

```python
logger = logging.getLogger()
logger.warning('user not found', extra=dict(user_id=13))
# user not found
```

So, if you use `extra`, stick to the third-party formatter you use or write your own.

## Custom formatter

NOTE: The text below wasn't published. Should it be a separate post?

So, to show `extra` when printing human-readable log messages as plain text, you have to write your own logs formatter:

```python
import logging
from copy import copy
from pythonjsonlogger.jsonlogger import RESERVED_ATTRS, merge_record_extra

class Formatter(logging.Formatter):
  def format(self, record):
    record = copy(record)
    # extract `extra` from the record
    extras = merge_record_extra(record=record, target={}, reserved=RESERVED_ATTRS)
    record.extras = ', '.join('{}={}'.format(k, v) for k, v in extras.items())
    record.msg += ' ({})'.format(record.extras)
    return super().format(record)

logger = logging.getLogger()

handler = logging.StreamHandler()
handler.setFormatter(Formatter())
logger.addHandler(handler)

logger.warning('user not found', extra=dict(user_id=13))
# user not found (user_id=13)
```
