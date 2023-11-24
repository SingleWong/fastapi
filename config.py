# -*- coding: utf-8 -*-
import os
from pydantic import BaseConfig


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEPLOY_ENV = os.environ.get('DEPLOY_ENV', 'dev')


class Config(BaseConfig):

    APP_NAME: str = 'TEMP'
    VERSION: str = '1.0.0'
    ADMIN_EMAIL: str = 'single.wong@test.com'
    DOCS_URL: str = '/docs'
    ENABLED_MODULES: list = ['user']
    LOGGER_LEVEL: str = 'DEBUG'
    ENV: str = 'None'
    BASE_DIR: str = BASE_DIR
    FORMAT: str = '%Y-%m-%dT%H:%M:%SZ'
    MYSQL_URL: str = 'mysql://admin:admin@127.0.0.1:3306/temp_00?charset=utf8mb4'
    REDIS_URL: str = 'redis://:admin@127.0.0.1:6379/0'


class TestingConfig(Config):

    pass


class ProductConfig(Config):
    pass


CONFIG_DICT = {
    'test': TestingConfig,
    'prd': ProductConfig
}


def static_config():
    config = CONFIG_DICT.get(DEPLOY_ENV, Config)()
    return config


STATIC_CONFIG = static_config()