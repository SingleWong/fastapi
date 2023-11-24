import json
from fastapi.routing import APIRoute
from typing import Callable
from fastapi import Request, Response, APIRouter
from starlette.responses import JSONResponse
from app.modules.base.utils import get_client_ip
from app.extensions.logging import logger as logging


async def rewrite_response(response) -> JSONResponse:
    if not isinstance(response, JSONResponse):
        return response
    content_type = response.headers.get('content-type')
    if content_type != 'application/json':
        return response
    body = response.body
    data = json.loads(body.decode("utf-8"))
    if data is None:
        return response
    result = {}
    if 'data' not in data:
        result['data'] = data
    else:
        result = data
    if 'code' not in data:
        result['code'] = 200
    if 'message' not in data:
        result['message'] = 'success'
    return JSONResponse(result, status_code=200)


async def write_log(request, response):
    content_type = request.headers.get("Content-Type", None)
    if content_type and "multipart/form-data" in content_type:
        body = await request.form()
    else:
        body = await request.body()
    log = {'ip': get_client_ip(request),
           'status_code': response.status_code,
           'request_url': request.url._url,
           'request_method': request.method,
           'request_body': body if body else ''
           }
    logging.debug(f'Router debug: {log}')


class ContextIncludedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            response: Response = await original_route_handler(request)
            response = await rewrite_response(response)
            await write_log(request, response)
            return response

        return custom_route_handler


class BaseAPIRouter(APIRouter):

    def __init__(self, route_class=ContextIncludedRoute):
        super(BaseAPIRouter, self).__init__(route_class=route_class)