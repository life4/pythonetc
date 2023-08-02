---
author: orsinium
id: 727
published: 2023-07-25
pep: 495
python: "3.6"
traces:
  - [module: datetime, type: datetime, arg: fold]
depends_on:
  - zoneinfo
topics:
  - time
---

# datetime.datetime.fold

Daylight saving time (DST) is the practice of advancing clocks (typically by one hour) during warmer months so that darkness falls at a later clock time and then turning it back for colder months. That means, sometimes, once a year the clock shows the same time twice. It can also happen when the UTC shift of the current timezone is decreased.

To distinguish such situations, [PEP-495](https://peps.python.org/pep-0495/) (landed in Python 3.6) introduce the [fold](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold) attribute for `datetime` that is 0 or 1 depending if this is the first or the second pass through the given time in the given timezone.

For example, in Amsterdam the time is shifted from CEST (Central European Summer Time) to CET (Central European Time) on the last Sunday of October:

```python
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ams = ZoneInfo('Europe/Amsterdam')
d0 = datetime(2023, 10, 29, 0, 0, tzinfo=timezone.utc)
for h in range(3):
    du = d0 + timedelta(hours=h)
    dl = du.astimezone(ams)
    m = f'{du.time()} UTC is {dl.time()} {dl.tzname()} (fold={dl.fold})'
    print(m)
```

This code will print:

```text
00:00:00 UTC is 02:00:00 CEST (fold=0)
01:00:00 UTC is 02:00:00 CET (fold=1)
02:00:00 UTC is 03:00:00 CET (fold=0)
```

However, you should keep in mind that `fold` is not considered in comparison operations:

```python
d1 = datetime(2023, 10, 29, 2, 0, tzinfo=ams)
d2 = datetime(2023, 10, 29, 2, 0, fold=1, tzinfo=ams)
d1 == d2  # True
```

Now imagine that your system has a bug because of not handling this. That happens once a year. On Sunday. At night 🌚
