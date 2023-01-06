from __future__ import annotations


def eval_or_exec(code: str, *, shield: str | None = None, shared_globals: dict) -> str:
    real_out = None
    try:
        try:
            real_out = eval(code, shared_globals)
        except SyntaxError:
            # not an expression, but a statement
            exec(code, shared_globals)
    except Exception as e:
        if shield is not None and shield == e.__class__.__name__:
            pass  # that was expected
        else:
            raise

    try:
        string_repr = repr(real_out) if real_out is not None else ''
    except Exception:
        string_repr = ''

    return string_repr
