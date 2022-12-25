---
published: 2018-05-02
id: 75
author: pushtaev
---

# LSP for dict

Liskov substitution principle tells us that if `S` is a subtype of `T`, then all occurrences of `T` may be replaced with `S` without breaking any code. That means that `S` should satisfy all the guarantees that `T` introduces.

Whenever you work with `dict` you usually assume that as long as `x in d` returns False, `d[x]` raises `KeyError`. But if your `dict` is a `defaultdict`, that it's simply not true. Does `defaultdict` violate the LSP then?

Strictly speaking, it doesn't. The `dict` documentation explicitly says that `d[x]` may return something even though `x` is not present in `d` (if the `__missing__` method defined). So you still potentially get something from the dictionary even if the key is not in it. That means that you shouldn't ever do `x in d` to check the existence of element as long as you want to support all `dict` subclasses.

It may seem that `defaultdict` violates the LSP, but it “breaks” the guarantees that were never there.
