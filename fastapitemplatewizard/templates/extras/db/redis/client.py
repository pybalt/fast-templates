from redis import Redis, ConnectionPool

pool = ConnectionPool(host=..., port=..., db=...)

redis_client = Redis(connection_pool=pool)