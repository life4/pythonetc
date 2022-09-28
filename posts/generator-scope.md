---
author: ypankovych
---

# generator scope

As you all may know, generators in Python being executed step-by-step. This means that there' should be possibility to "see" that state between the steps.

All generator's local variables stored in frame locals, and we can access the frame through the `gi_frame` attribute on a generator:

```python
def gen():
    x = 5
    yield x
    yield x

g = gen()
next(g)  # 5
g.gi_frame.f_locals  # {'x': 5}
```

So if we can see it, we should be able to modify it, right?

```python
g.gi_frame.f_locals["x"] = 10
next(g)  # still gives us 5
```

Frame locals returned as a dict is basically a newly created object from actual frame local vars, meaning that returned dict doesn't reference the actual variables in the frame.

But there's a way to bypass that with C API:

```python
import ctypes

# after we've changed the frame locals, we need to "freeze" it
# which is basically telling the interpreter to update the underlying frame based on a newly added attributes
ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(g.gi_frame), ctypes.c_int(0))
```

So now we can verify that the generator's locals has actually changed:

```python
next(g)  # 10
```

You might wonder what is `ctypes.c_int(0)`?  Basically, there's 2 "modes" you can use to update the underlying frame, 0 and 1. If you use 1, it'll add and/or update frame local vars that are already present in the frame. So if we'd remove the `x` from the locals dict and call the update with `c_int(0)`, it'd do nothing as it cannot delete the vars.

if you want to actually delete some variable from the frame, call the update with `c_int(1)`, that'll basically replace underlying frame locals with the new locals we've defined `.f_locals dict`.

And as you all know, coroutines in Python implemented using generators, so the same logic present there as well, but instead of `gi_frame` its `cr_frame`.
