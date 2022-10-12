---
author: orsinium
traces:
  - [{exception: ExceptionGroup}]
pep: 654
python: "3.11"
depends_on:
  - exception-group
---

# `except*`

[PEP 654](https://peps.python.org/pep-0654/) introduced not only `ExceptionGroup` itself but also a new syntax to handle it. Let's start right with an example:

```python
try:
  raise ExceptionGroup('', [
    ValueError(),
    KeyError('hello'),
    KeyError('world'),
    OSError(),
  ])
except* KeyError as e:
  print('caught1:', repr(e))
except* ValueError as e:
  print('caught2:', repr(e))
except* KeyError as e:
  1/0
```

The output:

```plain
caught1: ExceptionGroup('', [KeyError('hello'), KeyError('world')])
caught2: ExceptionGroup('', [ValueError()])
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  | ExceptionGroup:  (1 sub-exception)
  +-+---------------- 1 ----------------
    | OSError
    +------------------------------------
```

Here is what happened:

1. When `ExceptionGroup` is raised, it's checked against each `except*` block.
2. `except* KeyError` block catches `ExceptionGroup` that contains `KeyError`.
3. The matched `except*` block receives not the whole `ExceptionGroup` but its copy containing only matched sub-exceptions. In case of `except* KeyError`, it includes both `KeyError('hello')` and `KeyError('world')`
4. For each sub-exception, only the first match is executed (`1/0` in the example wasn't reached).
5. While there are unmatched sub-exceptions, they will be tried to match to remaining `except*` blocks.
6. If there are still sub-exceptions left after all of that, the `ExceptionGroup` with them is raised. So, `ExceptionGroup('', [OSError()])` was raised (and beautifully formatted).
