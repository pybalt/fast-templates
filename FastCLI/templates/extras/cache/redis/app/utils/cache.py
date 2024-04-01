import cachetools
import json
import hashlib
from app.db.redis import redis_client

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

def cache_in_redis(seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0):
    ttl = seconds + (minutes * 60) + (hours * 60 * 60) + (days * 60 * 60 * 24)
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = func.__name__ + hashlib.md5(str(args).encode() + str(kwargs).encode()).hexdigest()
            
            if (result := redis_client.get(key)) is not None:
                return json.loads(result)
            
            result = func(*args, **kwargs)
            redis_client.setex(key, ttl, json.dumps(result))

            return result
        return wrapper
    return decorator