The famous "Zen of Python" was introduced in [PEP-20](https://www.python.org/dev/peps/pep-0020/). This is 19 Guido van Rossum's aphorisms collected by Tim Peters. Do `import this` in the Python interpreter to see them:

```python
>>> import this                                                                 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

The fun thing is how this module looks like. The original text is encoded by [ROT13](https://en.wikipedia.org/wiki/ROT13) algorithm and is decoded on the fly:


```python
s = """Gur Mra bs Clguba, ol Gvz Crgref
...
"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
```

Some say it violates almost all the principles that it contains.
