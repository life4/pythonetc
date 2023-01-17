---
published: 2018-05-15
id: 90
author: pushtaev
---

# Patch built-ins

The `unittest.mock.patch` decorator can replace any attribute of any module with `MagicMock`.
That can be used for unit-testing as a replacement for other code isolation techniques such as dependency injection.

```python {hide}
from types import ModuleType
import sys
from unittest.mock import patch


class sms(ModuleType):
    def send():
        ...

sys.modules['sms'] = sms
        
def create_client(name):
    sms.send(name, 'client created')
```

```python {continue}
@patch('sms.send')
def test_now(patched_send):
    create_client('31205551111')
    patched_send.assert_called_with(
        '31205551111',
        'client created'
    )   
```

```python {continue}
test_now()
```

The significant limitation is that `patch` doesn't work with built-ins:

```python
# foo.py
from datetime import datetime
def is_odd_hour_now():
    print('@@@', datetime)
    print('@@@', datetime.now)
    return datetime.now().hour % 2 == 1
```

```python {hide} {continue}
from types import ModuleType
import sys
foo = type("foo", (ModuleType,), dict(datetime=datetime, is_odd_hour_now=is_odd_hour_now))
sys.modules['foo'] = foo
```

```python {continue}
# test_foo.py
from datetime import datetime
from unittest.mock import patch
from foo import is_odd_hour_now

@patch('datetime.datetime.now')
def test_is_odd_hour_now(patched_now):
    patched_now.return_value = \
        datetime(2010, 1, 1, 13, 0, 0)
    assert is_odd_hour_now()
```

```python {hide} {continue} {shield:TypeError}
test_is_odd_hour_now()
```

That will cause `TypeError: can't set attributes of built-in/extension type 'datetime.datetime'`.

As a workaround you can patch not the original `datetime`, but the reference that `foo` holds:

```python {continue}
from datetime import datetime
from unittest.mock import patch
from foo import is_odd_hour_now

@patch('foo.datetime')
def test_is_odd_hour_now(patched_datetime):
    patched_datetime.now.return_value = \
        datetime(2010, 1, 1, 13, 0, 0)
```

```python {hide}
# patching foo.datetime doesn't work for us,
# since we don't really have foo.py
# and the the `is_odd_hour_now` function doesn't use datetime from `foo`.

# So it's commented out.
### test_is_odd_hour_now()
```
