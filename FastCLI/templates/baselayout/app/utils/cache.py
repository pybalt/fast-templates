import cachetools


def timed_lru_cache(seconds: int = 0, minutes: int = 0, maxsize: int = 128):
    """
    Decorator that wraps the LRU cache implementation and adds a time expiration
    """

    ttl = seconds + (minutes * 60)

    def decorator(func):
        func = cachetools.cached(
            cache=cachetools.TTLCache(maxsize=maxsize, ttl=ttl)
        )(func)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    return decorator
