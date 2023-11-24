from tortoise.contrib.pydantic import pydantic_model_creator
from typing import Optional, List
from app.modules.user.models import User
from pydantic import BaseModel
from app.modules.base.schemas import PaginationParams, OrmSchema, PaginationSchema
from datetime import datetime


UserPydantic = pydantic_model_creator(User, name="User", exclude=('enabled', 'created_at', 'modified_at'))
UserInPydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True, exclude=('created_at', 'modified_at'))


class UserBaseField(BaseModel):
    enabled: bool
    name: Optional[str] = None
    username: Optional[str] = None
    family_name: Optional[str] = None


class UserSchema(UserBaseField, OrmSchema):
    id: int
    created_at: datetime


class UsersSchema(PaginationSchema):
    result: List[UserSchema]


class UserBaseField(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None


class UserQueryParam(UserBaseField, PaginationParams):
    # start_time: Optional[datetime] = None
    # end_time: Optional[datetime] = None
    pass
