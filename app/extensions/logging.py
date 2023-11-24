# -*- coding: utf-8 -*-
import time
from loguru import logger
import os
from config import STATIC_CONFIG


basedir = STATIC_CONFIG.BASE_DIR
log_path = os.path.join(basedir, 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)
path = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_log.log')
logger.add(path, rotation='100 MB', retention="5 days", level=STATIC_CONFIG.LOGGER_LEVEL)
