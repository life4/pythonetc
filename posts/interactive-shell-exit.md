---
author: pushtaev
id: 18
published: 2018-03-22
---

# Interactive shell: exit

```python-interactive {python-interactive-no-check}
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
```

Ever wonder why is this message displayed once you try to exit
interactive Python with just `exit` or `quit`?
The solution is quite unexpected yet graceful.
It's not a special case for interactive shell,
it just shows a representation of every result evaluated,
and this line is just
a [representation](https://github.com/python/cpython/blob/master/Lib/_sitebuiltins.py#L17)
of `exit` function.

Strictly speaking, you should not use `exit` in your everyday projects
since it was created specifically for interactive shell.
Use `sys.exit()` instead.
