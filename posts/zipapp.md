---
published: 2020-10-13
id: 616
author: orsinium
topic:
  - stdlib
  - module
qname: zipapp
python: "3.5"
---

# zipapp

The module [zipapp](https://docs.python.org/3/library/zipapp.html) can pack a python module into a zip archive that can be executed directly by a Python interpreter. It is a good way to ship CLI tools:

```bash
$ mkdir example
$ echo 'print("hello, @pythonetc!")' > example/__main__.py
$ python3 -m zipapp example
$ python3 example.pyz
hello, @pythonetc!
```
