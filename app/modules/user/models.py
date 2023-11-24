# -*- coding: utf-8 -*-
from tortoise import fields
from app.modules.base.models import BaseModel


class User(BaseModel):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    #: This is a username
    username = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=50, null=True)
    family_name = fields.CharField(max_length=50, null=True)
    category = fields.CharField(max_length=30, default="misc")
    password = fields.CharField(max_length=128, null=True)

    @classmethod
    def get_query(cls, **kwargs) -> dict:
        query = {}
        if kwargs.get('name'):
            query['name__icontains'] = kwargs['name']
        if kwargs.get('username'):
            query['name__icontains'] = kwargs['username']
        return query

    @property
    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.name or self.family_name:
            return f"{self.name or ''} {self.family_name or ''}".strip()
        return self.username
