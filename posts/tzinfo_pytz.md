---
published: 2018-04-04
id: 37
author: pushtaev
---

# tzinfo and pytz

Python provides the powerful library to work with date and time: `datetime`.
The interesting part is datetime objects have the special interface for timezone support
(namely `tzinfo` attribute), but this module only has limited support of its interface,
leaving the rest of the job to different modules.

The most popular module for this job is `pytz`.
The tricky part `pytz` don't fully satisfy `tzinfo` interface.
The `pytz` documentation states this at one the first lines:
“This library differs from the documented Python API for tzinfo implementations.”

You can't use `pytz` timezone objects as a tzinfo attribute.
If you try, you may get the absolute insane results:

```python {hide}
import pytz
from datetime import datetime, timedelta
```

```ipython {continue}
In : paris = pytz.timezone('Europe/Paris')
In : str(datetime(2017, 1, 1, tzinfo=paris))
Out: '2017-01-01 00:00:00+00:09'
```

Look at this `+00:09` offset. The proper use of pytz is following:

```ipython {continue}
In : str(paris.localize(datetime(2017, 1, 1)))
Out: '2017-01-01 00:00:00+01:00'
```


Also, after any arithmetic operations, you should `normalize` your datetime object in case of offset changes (on the edge of DST period for instance).

```python {continue} {hide}
time = pytz.timezone('Europe/Rome').localize(datetime(2018, 3, 25, 0, 0, 0))
```

```ipython {continue}
In : new_time = time + timedelta(days=2)
In : str(new_time)
Out: '2018-03-27 00:00:00+01:00'
In : str(paris.normalize(new_time))
Out: '2018-03-27 01:00:00+02:00'
```

Since Python 3.6 it's recommended to use `dateutil.tz` instead of `pytz`. It's fully compatible with `tzinfo`, can be passed as an attribute, doesn't require `normalize`, though works a bit slower.

If you are interested why `pytz` doesn't support `datetime` API, or you wish to see more examples, consider reading the decent [article](https://blog.ganssle.io/articles/2018/03/pytz-fastest-footgun.html) on the topic.
