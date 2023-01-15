---
published: 2018-05-19
id: 94
author: pushtaev
---

# contextlib.closing

Some things should be closed after the use. Some of them are provided as context managers (`open` is a notable example), and some of them aren't (say, `socket.socket`).

Writing such context manager is trivial:

```python {hide}
from socket import socket
from contextlib import contextmanager
```

```python {continue}
@contextmanager
def socket_context(*args, **kwargs):
    try:
        sock = socket(*args, **kwargs)
        yield sock
    finally:
        sock.close()
```

To avoid writing a context manager for every type of closing object , you can you universal `contextlib.closing`:

```python {hide}
import socket
from contextlib import closing
addr = socket.getaddrinfo("example.org", 80, proto=socket.IPPROTO_TCP)[0][-1]
data = b''
```

```python {continue}
with closing(socket.socket()) as sock:
    sock.connect(addr)
    sock.sendall(data)
```

If you still like to have a `socket_context` name, but don't want to write the monotonous try-yield-finally-close, you should wrap `closing`:

```python {continue}
def socket_context(*args, **kwargs):
    return closing(socket.socket(*args, **kwargs))
```
