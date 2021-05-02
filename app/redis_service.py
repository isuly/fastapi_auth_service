import redis

from app.config import REDIS_DB, REDIS_HOST, REDIS_PORT
from app.utils.singleton import Singleton


class RedisClient(metaclass=Singleton):

    def __init__(self):
        self.client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
