---
published: 2020-11-10
author: orsinium
qname: pydoc
---

# pydoc

The script [pydoc](https://docs.python.org/3/library/pydoc.html) can be used to see documentationand docstrings from the console:

```bash
$ pydoc3 functools.reduce | cat
Help on built-in function reduce in functools:

functools.reduce = reduce(...)
    reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    ...
```

Also, you can specify a port with `-p` flag, and `pydoc` will serve the HTML documentation browser on the given port:

```bash
$ pydoc3 -p 1234
Server ready at http://localhost:1234/
Server commands: [b]rowser, [q]uit
server>
```
