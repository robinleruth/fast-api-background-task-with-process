from functools import wraps


# Cache not good if it is only called in a different process, or good if
# wanted
def memoize(func):
    cache = dict()

    @wraps(func)
    def x(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return x
