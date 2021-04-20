# codecs

Published: 29 October 2020, 18:00

The module [codecs](https://docs.python.org/3/library/codecs.html) provides `encode` and `decode` function to encode and decode (wow!) text in different encodings, like UTF8, CP1251, [Punycode](https://en.wikipedia.org/wiki/Punycode), [IDNA](https://en.wikipedia.org/wiki/Internationalized_domain_name), [ROT13](https://en.wikipedia.org/wiki/ROT13), execute [escape sequences](https://en.wikipedia.org/wiki/Escape_sequence), etc.

```python
codecs.encode('hello, @pythonetc', 'rot13')
# 'uryyb, @clgubargp'

codecs.encode('\n', 'unicode_escape')
# b'\\n'

codecs.encode('привет, @pythonetc', 'punycode')
# b', @pythonetc-nbk5b4b7gra3b'

codecs.encode('привет, @pythonetc', 'idna')
# b'xn--, @pythonetc-nbk5b4b7gra3b'

codecs.encode('привет, @pythonetc', 'cp1251')
# b'\xef\xf0\xe8\xe2\xe5\xf2, @pythonetc'
```
