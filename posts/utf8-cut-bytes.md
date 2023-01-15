---
published: 2018-05-22
id: 97
author: pushtaev
---

# UTF-8: how to cut bytes

UTF-8 is a variable-width encoding. One character can be encoded by one, two, three or four bytes.
That means that you can't start reading a utf8-encoded string from any bite; that can accidentally break a character:

```ipython {shield:UnicodeDecodeError}
In : lion = 'Löwe'
In : lion.encode('utf-8')[2:]
Out: b'\xb6we'
In : lion.encode('utf-8')[2:].decode('utf-8')
...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb6 in position 0: invalid start byte
```

This also means that to skip the first N characters of a string you can read and decode them, calculating offset upfront is not possible.

You can, however, skip some fixed number of bytes with some precautions. Let's look how a symbol can be decoded:

```txt
0xxxxxxx
110xxxxx 10xxxxxx
1110xxxx 10xxxxxx 10xxxxxx
11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

As you can see, the byte is the leading byte of a character unless it's `10xxxxxx`. Such non-leading bytes are called *continuation bytes*. Let's skip them:

```python {continue}
def cut_bytes(s, n):
    result = s.encode('utf-8')[n:]
    mask = int('11000000', 2)
    conbyte = int('10000000', 2)
    while result[0] and result[0] & mask == conbyte:
        result = result[1:]

    return result.decode('utf-8')
```

```ipython {continue}
In : cut_bytes(lion, 2)
Out: 'we'
In : cut_bytes(lion, 1)
Out: 'öwe'
```
