import redis

from app.utils.singleton import Singleton

REDIS_HOST = '0.0.0.0'
REDIS_PORT = 6379
REDIS_DB = 0


class RedisClient(metaclass=Singleton):

    def __init__(self):
        self.client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
