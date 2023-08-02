---
author: orsinium
id: 726
published: 2023-07-18
pep: 615
python: "3.6"
traces:
  - [module: zoneinfo]
topics:
  - time
---

# zoneinfo

[PEP-615](https://peps.python.org/pep-0615/) (landed in Python 3.9) introduced the module [zoneinfo](https://docs.python.org/3/library/zoneinfo.html). The module provides access to information about time zones. It will try to use the information about time zones provided by the OS. If not available, it falls back to the official Python [tzdata](https://github.com/python/tzdata) package which you need to install separately.

```python
from zoneinfo import ZoneInfo
from datetime import datetime

ams = ZoneInfo('Europe/Amsterdam')
dt = datetime(2015, 10, 21, 13, 40, tzinfo=ams)
dt
# datetime(2015, 10, 21, 13, 40, tzinfo=ZoneInfo(key='Europe/Amsterdam'))

la = ZoneInfo('America/Los_Angeles')
dt.astimezone(la)
# datetime(2015, 10, 21, 4, 40, tzinfo=ZoneInfo(key='America/Los_Angeles'))
```

You should not use [pytz](https://pypi.org/project/pytz/) anymore.
