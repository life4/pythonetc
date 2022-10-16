---
author: VadimPushtaev
id: 11
published: 2018-03-18
---

# loop scope

The thing you usually don't care about is loops and if-blocks don't create scopes in Python (as well as try-blocks, with-block etc.). Because if they were, you won't be able to reassign variables inside the block:

```python {skip}
lst = [1, 2, 3]
```

```python {continue}
max = 0
for x in lst:
  if x > max:
    max = x  # reassigned
```

```python {skip} {continue}
assert max == 3
```

But you do care about it if you try to create some closures since nothing really closures until a scope ends.
