# -*- coding: utf-8 -*-
import traceback
from app.extensions.logging import logger
from fastapi import HTTPException, FastAPI, Request
from fastapi.responses import JSONResponse


class AutoExeption(HTTPException):

    def __init__(self, status_code=400, detail=None):
        super(AutoExeption, self).__init__(status_code=status_code, detail=detail)


class CurrentException(HTTPException):

    def __init__(self, detail=None):
        super(CurrentException, self).__init__(status_code=400, detail=detail)


class NotFoundException(HTTPException):

    def __init__(self, detail=None):
        super(NotFoundException, self).__init__(status_code=404, detail=detail)


class AuthErrorException(HTTPException):

    def __init__(self, detail=None):
        super(AuthErrorException, self).__init__(status_code=401, detail=f'Auth error! {detail}')


class ForbiddenException(HTTPException):

    def __init__(self, detail=None):
        super(ForbiddenException, self).__init__(status_code=403, detail=f'Forbidden! {detail}')


class StaticException(object):

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.register_static_exception(app)

    def register_static_exception(self, app: FastAPI) -> None:
        # 自定义异常 捕获
        # @app.exception_handler(UserNotFound)
        # async def user_not_found_exception_handler(request: Request, exc: UserNotFound):
        #     """
        #     用户认证未找到
        #     :param request:
        #     :param exc:
        #     :return:
        #     """
        #     logger.error(f"token未知用户\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        #     return response_code.resp_5001(message=exc.err_desc)

        @app.exception_handler(HTTPException)
        async def user_not_found_exception_handler(request: Request, exc: HTTPException):
            logger.error(f"Current error:\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
            data = exc.detail
            message = data.get('message') if isinstance(data, dict) and 'message' in data else repr(exc)
            return JSONResponse({"message": message, 'code': exc.status_code, 'data': data}, status_code=200)

        # 捕获全部异常
        @app.exception_handler(Exception)
        async def all_exception_handler(request: Request, exc: Exception) -> JSONResponse:
            """
            全局所有异常
            :param request:
            :param exc:
            """
            logger.error(f"全局异常\n{request.method}URL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
            return JSONResponse({"message": repr(exc), 'code': 400, 'data': None}, status_code=200)
