# coding: utf-8
from enum import Enum, IntEnum
from pydantic import BaseModel


class CustomIntEnum(IntEnum):

    @classmethod
    def choices(cls):
        return [(s.value, s.name) for s in cls]

    @classmethod
    def str_int_mapping(cls):
        return {
            s.name:s.value
            for s in cls
        }

    @classmethod
    def int_str_mapping(cls):
        return {
            s.value: s.name
            for s in cls
        }

    @classmethod
    def str2int(cls, op_type: str) -> int:
        # 字符转数字
        return cls.str_int_mapping().get(op_type, -1)

    @classmethod
    def int2str(cls, op_type: int) -> str:
        # 数字转字符
        return cls.int_str_mapping().get(op_type, '')


class TypesSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class OrmSchema(BaseModel):
    class Config:
        orm_mode = True


class BaseTimeModel(BaseModel):
    start_time: int = None
    end_time: int = None


class PerpageEnum(IntEnum):
    five = 5
    ten = 10
    twenty = 20
    fifty = 50
    hundred = 100
    thousand = 1000


class PaginationParams(BaseModel):
    page: int = 1
    per_page: PerpageEnum = PerpageEnum.ten


class PaginationSchema(PaginationParams, TypesSchema):
    pages: int
    total: int
