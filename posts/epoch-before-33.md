---
published: 2018-03-31
id: 33
author: pushtaev
buttons:
  - title: Try this code live
    url: "https://replit.com/@VadimPushtaev/strftime"
topics:
  - time
---

# epoch before Python 3.3

Converting `datetime` object to the number of seconds since the start of the epoch
is not a simple task until Python 3.3.

The most natural solution for the problem is to use `strftime` method
that can format the datetime. Using `%s` as a format you can get a timestamp.
Look at the example:

```python {hide}
from datetime import datetime
import pytz
```

```python {continue}
naive_time = datetime(2018, 3, 31, 12, 0, 0)
utc_time = pytz.utc.localize(naive_time)
ny_time = utc_time.astimezone(
    pytz.timezone('US/Eastern'))
```

`ny_time` is the exact the same moment as `utc_time`,
but written as New Yorkers see it:

```text
# utc_time
datetime.datetime(2018, 3, 31, 12, 0,
    tzinfo=<UTC>)
# ny_time
datetime.datetime(2018, 3, 31, 8, 0,
    tzinfo=<DstTzInfo 'US/Eastern' ...>)
```

Since they are the same moments, their timestamps should be equal:

```ipython {continue} {no-run} {# doesn't work on Windows #}
In : int(utc_time.strftime('%s')),
     int(ny_time.strftime('%s'))
Out: (1522486800, 1522468800)
```

Wait, what? They are not the same at all.
In fact, you can't use `strftime` as a solution for this problem.
Python's `strftime` doesn't even support `%s` as an argument,
it merely works because internally the platform C library’s strftime() is called.
But, as you can see, the timezone of datetime object is wholly ignored.

The proper result can be achieved with straightforward subtraction:

```python {continue}
In : epoch_start = pytz.utc.localize(
      datetime(1970, 1, 1))

In : (utc_time - epoch_start).total_seconds()
Out: 1522497600.0

In : (utc_time - epoch_start).total_seconds()
Out: 1522497600.0
```

Again, if you use Python 3.3+, you can solve the problem
with `timestamp()` method of `datetime`: `utc_time.timestamp()`.
