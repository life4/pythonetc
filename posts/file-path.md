---
published: 2018-05-21
id: 96
author: pushtaev
---

# Making file path

Concatenating parts of file path can be done with `os.path.join`:

```python
import os
```

```ipython {continue}
In : dir_path = '/home/vadim/'
In : file_name = 'test.py'
In : os.path.join(dir_path, file_name)
Out: '/home/vadim/test.py'
```

It's usually better than using string concating like this:

```ipython {continue}
In : dir_path + '/' + file_name
Out: '/home/vadim//test.py'
```

`os.path.join` uses the correct delimiter for the current platform (e. g. `\` for Windows). It also never produces a double delimiter (`//`).

Since Python 3.4, you also can use the `Path` class from the `pathlib` module.
(It also can be used as an `os.path.join` argument since Python 3.6.)
`Path` supports concatenation via `/` operator:

```python {hide}
from pathlib import Path, PosixPath
```

```python {continue}
In : Path('/home/vadim/') / Path('test.py')
Out: PosixPath('/home/vadim/test.py')
```
