---
published: 03 December 2020, 18:00
author: orsinium
---

# json default

`json.dumps` can serialize every built-in type which has a corresponding JSON type (`int` as `number`, `None` as `null`, `list` as `array` etc) but fails for every other type. Probably, the most often case when you will face it is when trying to serialize a datetime object:

```python
import json
from datetime import datetime

json.dumps([123, 'hello'])
# '[123, "hello"]'

json.dumps(datetime.now())
# TypeError: Object of type 'datetime' is not JSON serializable
```

The fastest way to fix it is to provide a custom default serializer:

```python
json.dumps(datetime.now(), default=str)
# '"2020-12-03 18:00:10.592496"'
```

However, that means that every unknown object will be serialized into a string which can lead to unexpected result:

```python
class C: pass
json.dumps(C(), default=str)
'"<__main__.C object at 0x7f330ec801d0>"'
```

So, if you want to serialize only `datetime` and nothing else, it's better to define a custom encoder:

```python
class DateTimeEncoder(json.JSONEncoder):
  def default(self, obj) -> str:
    if isinstance(obj, datetime):
      return obj.isoformat()
    return super().default(obj)

json.dumps(datetime.now(), cls=DateTimeEncoder)
'"2020-12-03T18:01:19.609648"'

json.dumps(C(), cls=DateTimeEncoder)
# TypeError: Object of type 'C' is not JSON serializable
```
