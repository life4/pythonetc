---
published: 2018-05-26
id: 100
author: pushtaev
buttons:
- title: "Tail Recursion Elimination by Guido"
  url: "http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html"
- title: "Final Words on Tail Calls by Guido"
  url: "http://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html"
---

# Tail recursion

Tail recursion is a special case of recursion where the recursive call is the last expression in the function:

```python
def fact(x, result=1):
    if x == 0:
        return result
    else:
        return fact(x - 1, result * x)
```

The cool thing about it is you don't have to return to the caller once callee returns the result since the caller has nothing more to do.
That means that you don't have to save the stack frame of the caller.

That technique is called TRE, tail recursion elimination. And Python doesn't support it.
It was considered and declined by Guido, mostly because removing stack frames makes stack trace looks cryptic.
