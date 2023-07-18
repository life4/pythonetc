---
author: orsinium
published: 2023-08-01
traces:
  - [module: unittest.mock, function: seal]
python: "3.7"
---

# unittest.mock.seal

Let's say, you have the following mock:

```python
from unittest.mock import Mock
user = Mock()
user.name = 'Guido'
```

You fully specified all attributes and methods it should have, and you pass it into the tested code, but then that code uses an attribute that you don't expect it to use:

```python {continue}
user.age
# <Mock name='mock.age' id='...'>
```

Instead of failing with an `AttributeError`, the mock instead will create a new mock when its unspecified attribute is accessed. To fix it, you can (and should) use the [unittest.mock.seal](https://docs.python.org/3/library/unittest.mock.html#sealing-mocks) function (introduced in Python 3.7):

```python {continue} {shield:AttributeError}
from unittest.mock import seal
seal(user)

user.name
# 'Guido'

user.occupation
# AttributeError: mock.occupation
```
