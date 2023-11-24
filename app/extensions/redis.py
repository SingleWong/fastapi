# -*- coding: utf-8 -*-
from redis import ConnectionPool, Redis


class RedisHandler(object):

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app, url=None):
        redis_url = app.config.REDIS_URL if not url else url

        pool = ConnectionPool.from_url(redis_url,
                                       max_connections=10,
                                       socket_timeout=10,
                                       retry_on_timeout=True)
        self.client = Redis(connection_pool=pool, decode_responses=True)

    def has_key(self, key):
        """
        Check if has key in redis
        :param key:
        :return:
        """
        if self.client.get(key):
            return True
        return False

    def set(self, key, value, expire=None):
        """
        Set key , value and expire time
        :param key:
        :param value:
        :param expire: seconds
        :return:
        """
        if value is not None:
            self.client.set(key, value)
            if expire is not None:
                self.client.expire(key, expire)

    def get(self, key):
        return self.client.get(key)

    def ttl(self, key):
        return self.client.ttl(key)

    def rm_key(self, key):
        return self.client.delete(key)