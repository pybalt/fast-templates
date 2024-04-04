from redis import Redis, ConnectionPool
from app.settings import settings

pool = ConnectionPool(settings.REDIS_URI)

redis_client = Redis(connection_pool=pool)