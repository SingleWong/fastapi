# -*- coding: utf-8 -*-
from fastapi import Depends

from app.modules.base.auth import verify_session


def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-variable
    """
    Init users_ module.
    """
    # Touch underlying modules
    from . import models, resources  # pylint: disable=unused-variable
    _name = __name__.split('.')[-1]
    app.include_router(
        resources.router,
        prefix='/api/'+_name,
        tags=[_name],
        # dependencies=[Depends(verify_session)],
        responses={404: {"description": "Not found"}},
    )
