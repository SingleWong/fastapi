# -*- coding: utf-8 -*-
from tortoise import models, fields
from app.extensions.exceptions import NotFoundException


class BaseModel(models.Model):
    enabled = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True, description='创建时间')
    modified_at = fields.DatetimeField(auto_now=True, description='更新时间')

    class Meta:
        abstract = True

    def update(self, **kwargs):
        for key in kwargs:
            if kwargs[key] is not None:
                setattr(self, key, kwargs[key])
        return self.save()

    def disable(self):
        return self.update(enabled=False)

    def enable(self):
        return self.update(enabled=True)

    @classmethod
    async def is_exist(cls, *args, **kwargs) -> bool:
        return await cls.exists(*args, **kwargs)

    @classmethod
    def get_enabled_object(cls, *args, **kwargs):
        return cls.get_object(enabled=True, *args, **kwargs)

    @classmethod
    def get_enabled_objects(cls, *args, **kwargs):
        return cls.get_objects(enabled=True, *args, **kwargs)

    @classmethod
    def get_object(cls, *args, **kwargs):
        return cls.filter(*args, **kwargs).first()

    @classmethod
    def get_objects(cls, *args, **kwargs):
        return cls.filter(*args, **kwargs).order_by('-modified_at').all()

    @classmethod
    async def get_object_by_id(cls, id):
        if not await cls.is_exist(id=id):
            raise NotFoundException('%s not exist, id %s' % (cls.__name__, id))
        return cls.get_enabled_object(id=id)

    @classmethod
    async def get_pagination(cls, total, page, per_page, objects, **kwargs):
        pages = int(total / per_page) + 1
        result = await objects.offset((page - 1) * per_page).limit(per_page)
        return {
            "total": total,
            "pages": pages,
            "page": page,
            "per_page": per_page,
            "result": result,
        }
