---
author: orsinium
id: 703
published: 2022-10-25
pep: 657
python: "3.11"
---

# Column in tracebacks

[PEP 657](https://peps.python.org/pep-0657/) (landed into Python 3.11) enhanced tracebacks so that they now include quite a precise location of where the error occurred:

```text
Traceback (most recent call last):
  File "query.py", line 24, in add_counts
    return 25 + query_user(user1) + query_user(user2)
                ^^^^^^^^^^^^^^^^^
  File "query.py", line 32, in query_user
    return 1 + query_count(db, response['a']['b']['c']['user'], retry=True)
                               ~~~~~~~~~~~~~~~~~~^^^^^
TypeError: 'NoneType' object is not subscriptable
```

It shows not only where the error occurred for each frame, but also which code was executed. Beautiful!
