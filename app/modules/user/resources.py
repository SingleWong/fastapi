# -*- coding: utf-8 -*-
from fastapi import Depends
from app.modules.base.resources import BaseAPIRouter
from app.modules.user.schemas import UserPydantic, UserInPydantic, UserQueryParam, UsersSchema
from app.modules.user.models import User


router = BaseAPIRouter()


@router.post("/", response_model=UserPydantic)
async def create_user(user: UserInPydantic):
    kwargs = user.model_dump(exclude_unset=True)
    user = await User.create(**kwargs)
    return await UserPydantic.from_tortoise_orm(user)


@router.get("/{id}", response_model=UserPydantic)
async def get_user(id: int):
    user = await User.get_object_by_id(id)
    return await UserPydantic.from_queryset_single(user)


@router.put("/{id}", response_model=UserPydantic)
async def update_user(id: int, user: UserInPydantic):
    kwargs = user.model_dump(exclude_unset=True)
    user = await User.get_object_by_id(id)
    user = await user.update(**kwargs)
    return await UserPydantic.from_queryset_single(user)


@router.delete("/{id}",)
async def delete_user(id: int):
    user = await User.get_object_by_id(id)
    await user.delete()
    return {'message': f"Deleted user {id}"}


@router.get("/", response_model=UsersSchema)
async def get_users(param: UserQueryParam = Depends(UserQueryParam)):
    kwargs = param.model_dump()
    query = User.get_query(**kwargs)
    kwargs['objects'] = User.get_enabled_objects(**query)
    kwargs['total'] = await kwargs['objects'].count()
    return await User.get_pagination(**kwargs)

