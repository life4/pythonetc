---
published: 2020-12-31
id: 645
author: orsinium
---

# new year 2020-2021

```python
from base64 import b64decode
from random import choice

CELLS = '~' * 12 + '¢•*@&.;,"'

def tree(max_width):
  yield '/⁂\\'.center(max_width)

  for width in range(3, max_width - 1, 2):
    row = '/'
    for _ in range(width):
        row += choice(CELLS)
    row += '\\'
    yield row.center(max_width)

  yield "'|  |'".center(max_width)
  yield " |  | ".center(max_width)
  yield '-' * max_width
  title = b'SGFwcHkgTmV3IFllYXIsIEBweXRob25ldGMh'
  yield b64decode(title).decode().center(max_width)

for row in tree(40):
  print(row)
```
