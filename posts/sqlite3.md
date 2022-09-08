---
published: 2021-05-04
author: orsinium
qname: sqlite3
---

# sqlite3

Python has a built-in module [sqlite3](https://docs.python.org/3/library/sqlite3.html) to work with [SQLite](https://sqlite.org/index.html) database.

```python
import sqlite3
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('SELECT UPPER(?)', ('hello, @pythonetc!',))
cur.fetchone()
# ('HELLO, @PYTHONETC!',)
```

Fun fact: for explanation what is [SQL Injection](https://en.wikipedia.org/wiki/SQL_injection) the documentation links [xkcd about Bobby tables](https://xkcd.com/327/) instead of some smart article or Wikipedia page.
