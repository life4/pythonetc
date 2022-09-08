---
published: 2022-09-20
author: orsinium
qname: string.Template
---

# string.Template

The [string.Template](https://docs.python.org/3/library/string.html#template-strings) class allows to do `$`-style substitutions:

```python
from string import Template
t = Template('Hello, $channel!')

t.substitute(dict(channel='@pythonetc'))
# 'Hello, @pythonetc!'

t.safe_substitute(dict())
# 'Hello, $channel!'
```

Initially, it [was introduced](https://peps.python.org/pep-0292/) to simplify translations of strings. However, now [PO-files](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html) natively support [python-format](https://www.gnu.org/software/gettext/manual/html_node/python_002dformat.html) flag. It indicates for translators that the string has `str.format`-style substitutions. And on top of that, `str.format` is much more powerful and flexible.

Nowadays, the main purpose of `Template` is to confuse newbies with [one more way to format a string](https://t.me/pythonetc/610). Jokes aside, there are a few more cases when it can come in handy:

+ `Template.safe_substitute` can be used when the template might have variables that aren't defined and should be ignored.
+ The substitution format is similar to the string substitution in bash (and other shells), which is useful in some cases. For instance, if you want to write your own [dotenv](https://github.com/motdotla/dotenv).
