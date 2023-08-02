---
author: ypankovych
id: 700
published: 2022-10-11
---

# generator scope

As you may know, generators in Python are executed step-by-step. This means that there should be a possibility to "see" that state between the steps.

All generator's local variables are stored in frame locals, and we can access the frame through the `gi_frame` attribute on a generator:

```python
def gen():
    x = 5
    yield x
    yield x
    yield x

g = gen()
next(g)  # 5
g.gi_frame.f_locals  # {'x': 5}
```

So if we can see it, we should be able to modify it, right?

```python  {continue}
g.gi_frame.f_locals["x"] = 10
next(g)  # still gives us 5
```

Frame locals returned as a dict is a newly created object from actual frame local vars, meaning that returned dict doesn't reference the actual variables in the frame.

But there's a way to bypass that with C API:

```python  {continue}
import ctypes

# after we've changed the frame locals, we need to "freeze" it
# which is basically telling the interpreter to update the underlying frame based on newly added attributes
ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(g.gi_frame), ctypes.c_int(0))
```

So now we can verify that the generator's locals have actually changed:

```python  {continue}
next(g)  # 10
```

You might wonder what is `ctypes.c_int(0)`? There are 2 "modes" you can use to update the underlying frame, 0 and 1. If you use 1, it'll add and/or update frame local vars that are already present in the frame. So if we'd remove the `x` from the locals dict and call the update with `c_int(0)`, it'd do nothing as it cannot delete the vars.

if you want to actually delete some variable from the frame, call the update with `c_int(1)`. That will replace underlying frame locals with the new locals we've defined `.f_locals` dict.

And as you may know, coroutines in Python are implemented using generators, so the same logic is present there as well, but instead of `gi_frame` it's `cr_frame`.
