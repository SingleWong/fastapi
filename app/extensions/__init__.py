# -*- coding: utf-8 -*-
from app.extensions.redis import RedisHandler
redis_handler = RedisHandler()

from app.extensions.exceptions import StaticException
static_exception = StaticException()

from app.extensions.mysql import MysqlHandler
db = MysqlHandler()


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in [
        static_exception,
        redis_handler,
        db
    ]:
        extension.init_app(app)
