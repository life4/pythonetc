---
published: 30 September 2020, 18:00
author: orsinium
---

# int to str #2

The point of the post above was that for some simple tasks there are many ways to do it (and some ways are good only in some cases). Also, the number of possible solutions grows as the language evolves. Another good example is concatenation. You can join 2 strings with f-strings, `str.format`, `str.join`, `+`, and so on. Thinking about these ways, even not suitable for daily usage, helps better language understanding.

Our amazing subscribers decided to take the challenge. Below are some not suitable for work but fan solutions how to convert int to str.

@dedefer:

```python
import io
with io.StringIO() as f:
    print(n, end='', file=f)
    n_str = f.getvalue()
```

Evgeny:

```python
import ctypes
ctypes.cdll.LoadLibrary('libc.so.6').printf(b'%d', n)
```

If you're going to use solutions below on the production, keep in mind that it doesn't work with negative numbers.

@oayunin:

```python
from math import log10
''.join(['0123456789'[(n // 10 ** i) % 10] for i in range(int(log10(n)), -1, -1)])
```

A similar solution from @apatrushev:

```python
''.join(chr(t + 48) for t in (n // 10**x % 10 for x in reversed(range(int(math.log(n,10)) + 1))) if t)
```

A similar solution with lambdas from @antonboom:

```python
(lambda n:
  ''.join(
    chr(ord('0') + (n // (10**i)) % 10)
    for i in range(math.ceil(math.log(n, 10)) - 1, -1, -1)
  )
)(n)
```

One more from @oayunin:

```python
from subprocess import check_output
with open('/tmp/tmp.txt', 'w') as f:
  for x in range(n):
    f.write(' ')
check_output(['wc', '-c', '/tmp/tmp.txt']).decode().split()[0]
```

@orsinium:

```python
import sys
import subprocess
cmd = [sys.executable, '-c', 'print(len("' + '*' * n + '"))']
subprocess.run(cmd, capture_output=True).stdout.strip().decode()
```

@maxvyaznikov:

```python
chars = []
while n > 0:
    digit = n % 10
    n = int(n / 10)
    chars.append(chr(ord('0') + digit))
print(''.join(chars[::-1]))
```
