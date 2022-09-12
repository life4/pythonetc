---
published: 2020-12-24
id: 643
author: orsinium
topic:
  - stdlib
  - constant
qname: math.tau
pep: 628
python: "3.6"
---

# math.tau (PEP-628)

The issue with a beautiful number [#12345](https://bugs.python.org/issue12345) proposed to add the following constant into stdlib:

```python
tau = 2*math.pi
```

It was a controversial proposal since apparently it's not hard to recreate this constant on your own which will be more explicit, since more people are familiar with π rather than τ. However, the proposal was accepted and tau landed in `math` module in Python 3.6 ([PEP-628](https://www.python.org/dev/peps/pep-0628/)):

```python
import math
math.tau
# 6.283185307179586
```

There is a long story behind τ which you can read at [tauday.com](https://tauday.com/). Especially good [this numberphile video](http://youtu.be/83ofi_L6eAo).
