---
published: 2018-03-25
id: 24
author: pushtaev
---

# Keyword-only arguments

Python 3 allows you to make some function arguments keyword-only, meaning they must be passed as `(arg=value)` rather than just `(value)`.

It may be useful to prevent function calls like this: `grep(text, pattern, True, False, True)`, where `True, False, True` actually means ignore case, don't invert match, pattern is Perl regexp.
It would be nice to force the only reasonable form of this call:

```python {hide}
def grep(text, pattern, *, ignore_case=False, perl_regexp=False):
    pass
    
text = ''
pattern = ''    
```

```python {continue}
grep(text, pattern,
    ignore_case=True,
    perl_regexp=True)
```


To achieve this result you should place the keyword-only arguments after varargs argument (aka `*args`):

```python
def grep(
    text, pattern, *args,
    ignore_case=False,
    invert_match=False,
    perl_regexp=False,
):
    pass
```


If you don't need `*args` (like in the example), just replace it with a bare asterisk:

```python
def grep(
    text, pattern, *,
    ignore_case=False,
    invert_match=False,
    perl_regexp=False,
):
    pass
```
