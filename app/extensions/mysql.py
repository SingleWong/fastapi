# -*- coding: utf-8 -*-
from tortoise.contrib.fastapi import register_tortoise
from config import STATIC_CONFIG

models = ["aerich.models"]
for model_name in STATIC_CONFIG.ENABLED_MODULES:
    models.append(f'app.modules.{model_name}.models')

TORTOISE_ORM = {
    'connections': {
        'default': STATIC_CONFIG.MYSQL_URL
    },
    'apps': {
        'models': {
            'models': models,
            'default_connection': 'default',
        }
    }
}


class MysqlHandler(object):

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        register_tortoise(
            app,
            config=TORTOISE_ORM,
            generate_schemas=False,
            add_exception_handlers=False,
        )
