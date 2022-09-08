---
published: 06 October 2020, 18:00
author: orsinium
qname: enum
---

# enum

The module [enum](https://docs.python.org/3/library/enum.html) provides a way to build an enumerable class. It is a class with a predefined list of instances, and every instance is bound to a unique constant value.

```python
from colorsys import rgb_to_hls
from enum import Enum

class Color(Enum):
    RED = (1, 0, 0)
    GREEN = (0, 1, 0)
    BLUE = (0, 0, 1)

    @property
    def hls(self):
        return rgb_to_hls(*self.value)

Color
# <enum 'Color'>

Color.RED
# <Color.RED: (1, 0, 0)>

Color.RED.name
# 'RED'

Color.RED.value
# (1, 0, 0)

Color.RED.hls
# (0.0, 0.5, 1.0)

type(Color.RED) is Color
# True
```
