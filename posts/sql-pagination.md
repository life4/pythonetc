---
published: 2018-04-20
id: 61
author: pushtaev
---

# SQL pagination

Pagination is the pretty standard problem that countless developers solve every day. If you use a relational database, you can explicitly set the offset with `LIMIT`:

```sql
SELECT *
FROM table
LIMIT 1001, 1100
```

That indeed returns a hundred of records, from 1001 to 1100. The thing is, it's as hard for a database as selecting all 1001 tuples.
So the later page your user requests, the slower you return the result.

The solution is to use `WHERE` instead of `LIMIT`, asking a client to provide the last result of her current page (`$last_seen_id` in the example):

```sql
SELECT *
FROM table
WHERE id > $last_seen_id
ORDER BY id ASC
LIMIT 100
```

See the perfect [article](https://use-the-index-luke.com/no-offset) regarding the subject.
