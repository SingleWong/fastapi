# -*- coding: utf-8 -*-

import datetime
import os
import shutil
import time
import uuid
from functools import wraps
from app.extensions.logging import logger as logging
from config import STATIC_CONFIG
import re


def is_ip(input):
    p = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(input):
        return True


def utcnow():
    return datetime.datetime.utcnow()


def now():
    return datetime.datetime.now()


def timedelta_to_seconds(timedelta):
    return timedelta.total_seconds()


def datetime_to_timestamp(date):
    # datetime类型转时间戳
    # return int(time.mktime(date_.timetuple()))
    return int(time.mktime(date.timetuple())) * 1000


def timestamp_to_datetime(timestamp, utc=False):
    # 时间戳转datetime类型
    if len(str(timestamp)) > 10:
        timestamp = timestamp / 1000
    if utc:
        return datetime.datetime.utcfromtimestamp(timestamp)
    return datetime.datetime.fromtimestamp(timestamp)


def utctimestamp_to_datetime(timestamp):
    # 时间戳转datetime类型
    if len(str(timestamp)) > 10:
        timestamp = timestamp / 1000
    return datetime.datetime.utcfromtimestamp(timestamp)


def datetime_to_str(date, format=STATIC_CONFIG.FORMAT):
    return date.strftime(format)


def str_to_datetime(date, format=STATIC_CONFIG.FORMAT):
    return datetime.datetime.strptime(date, format)


def params_to_logfile(func):
    """
    记录接口的请求参数并写入到日志文件的装饰器
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logging.info(f'Parameter shows as below: {kwargs}')
        result = await func(*args, **kwargs)
        return result
    return wrapper


def get_client_ip(request):
    ip = request.headers.get(
        'X-Forwarded-For', request.client.host)
    if ', ' in ip:
        ip = ip.split(', ')[0]
    return ip


def clean_none_from_dict(kwargs):
    if not isinstance(kwargs, dict):
        return kwargs
    d = {}
    for k, v in kwargs.items():
        if v is not None:
            d[k] = v
    return d


def get_uuid():
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    return suid


def f_copy(file_path, new_path):
    p_ = os.path.dirname(new_path)
    if not os.path.exists(p_):
        os.makedirs(p_)
    if os.path.isfile(file_path):
        shutil.copyfile(file_path, new_path)


def f_write(path, data, action='w', encoding=None):
    f_dir = os.path.dirname(path)
    if not os.path.exists(f_dir):
        os.makedirs(f_dir)
    with open(path, action, encoding=encoding) as f:
        f.write(data)