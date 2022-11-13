import functools


def unparameterized_decorator(decorator):
    @functools.wraps(decorator)
    def wrapped(func=None):
        if func is None:
            return decorator
        return decorator(func)

    return wrapped

@unparameterized_decorator
def atomic(func):
    @functools.wraps(func)
    def wrapped():
        print('BEGIN')
        func()
        print('COMMIT')

    return wrapped
