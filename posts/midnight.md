---
published: 2018-05-05
id: 80
author: pushtaev
---

# Midnight

Let's suppose you have some datetime object and want to know how much time has passed since the start of the day. How do you do that?

First of all, to know what day we are talking about, we need to have the timezone; having the datetime is not enough.
As long as you have the timezone you need to convert the datetime and strip time with the `date()` method:

```python {hide}
import datetime
```

```python {continue}
def date_of_time(datetime_object, tz):
    return datetime_object.astimezone(tz).date()
```

Having the date, we can get its midnight time. To do this, we glue `00:00:00` back to the datetime object and assign the original timezone:

```python {continue}
def midnight_of_date(date_in_given_timezone, tz):
    midnight = datetime.datetime.combine(
        date_in_given_timezone, datetime.time()
    )

    return tz.localize(midnight)
```

And now we put things together:

```python {continue}
def midnight(datetime_object, tz):
    return midnight_of_date(
        date_of_time(datetime_object, tz), tz
    )
```

```python {hide} {continue}
import pytz
assert (
    midnight(datetime.datetime(2018, 5, 5, 12, 0, 0), pytz.timezone('Europe/Helsinki'))
    == datetime.datetime(2018, 5, 4, 21, 0, 0, tzinfo=pytz.utc)
)
```
