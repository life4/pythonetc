[Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) is the number of positions at which the corresponding symbols are different. It's the simplest measure of difference between 2 strings and can be implemented in a few lines:

```python
from itertools import zip_longest

def hamming(left, right):
    return sum([sl != sr for sl, sr in zip_longest(left, right)])

hamming('hello', 'hello')
# 0

hamming('hello', 'hallo')
# 1

hamming('hello', 'helol')
# 2
```
