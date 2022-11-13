---
published: 2018-03-26
id: 25
author: pushtaev
---

# pytest

`py.test` is a simple yet powerful tool that allows you to run tests.
It may be useful not only for big projects but even for one-off scripts.

Let's say you write a small utility to parse some log,
and you have a function to detect _GET_ requests.

```python {hide}
import re
```

```python {continue}
def is_get(line):
    return re.search(r'\bGET\b', line)
```

To test it you may put some debug statements in your script,
copy the function to another file or Python shell and run it manually,
or create a stand-alone test script.
Or you may just define `test_is_get` along `is_get`
that doesn't interfere with your script unless it is executed with `py.test`.

```python {continue}
def test_is_get():
    assert is_get('12:00 GET url')
    assert is_get('00:00 url GET params')
    assert not is_get('07:00 GETTER restart')
```

Once the script is started with `py.test log_parser.py`,
all `test_*` will be executed.
This way you can actually have two modes to run your script:
with `python` to parser log or with `py.test` to test some things
you want to be tested.
