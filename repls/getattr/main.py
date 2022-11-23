class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __getattr__(self, attr):
        prefix, orig_attr = attr.split('_', 2)
        if prefix == 'hex' and hasattr(self, orig_attr):
            return hex(getattr(self, orig_attr))
        else:
            raise AttributeError

p = Point(16, 20)
print(p.hex_x, p.hex_y)
