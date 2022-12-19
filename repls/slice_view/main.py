from collections.abc import MutableSequence

class SliceView(MutableSequence):
    def __init__(self, lst, start, stop):
        self._lst = lst
        self._start = start
        self._stop = stop

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            if idx.step:
                raise IndexError('step not supported')
            return type(self)(
                self._lst,
                self._start + idx.start,
                min(self._stop, self._start + idx.stop),
            )
        else:
            if self._start + idx >= self._stop:
                raise IndexError()
            return self._lst[self._start + idx]

    def __setitem__(self, idx, value):
        if isinstance(idx, slice):
            if idx.step:
                raise IndexError('step not supported')
            self._lst[
                self._start + idx.start:
                min(self._stop, self._start + idx.stop)
            ] = value
        else:
            if self._start + idx >= self._stop:
                raise IndexError()
            self._lst[self._start + idx] = value

    def __len__(self):
        return self._stop - self._start

    def __delitem__(self, idx):
        raise RuntimeError('Not implemented in this example')

    def insert(self, idx, value):
        raise RuntimeError('Not implemented in this example')


lst = list(range(10))
assert list(SliceView(lst, 1, 5)) == [1, 2, 3, 4]
assert list(SliceView(lst, 1, 5)[1:3]) ==  [2, 3]
assert lst == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

SliceView(lst, 2, 5)[0:2] = [-1, -2]
SliceView(lst, 2, 5)[2] = -3
assert lst == [0, 1, -1, -2, -3, 5, 6, 7, 8, 9]
print(lst)
