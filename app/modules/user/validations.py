# -*- coding: utf-8 -*-
from enum import Enum, IntEnum


class UserStatusEnum(Enum):
    super: str = 'super'
    admin: str = 'admin'
    ops: str = 'ops'
