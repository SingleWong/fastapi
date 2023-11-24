# -*- coding: utf-8 -*-
from app.extensions.logging import logger as logging
from app.extensions.exceptions import AuthErrorException
from typing import Optional
from fastapi import Cookie, Header


async def verify_session(
        SESSIONID: Optional[str] = Cookie(None),
        x_token: Optional[str] = Header(None)
 ):
    logging.debug(f'SESSIONID: {SESSIONID}, x_token: {x_token}')
    if not SESSIONID:
        raise AuthErrorException(f'Has no session: {SESSIONID}')