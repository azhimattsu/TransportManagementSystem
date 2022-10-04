from fastapi import Request, Response
from .exception import CustomHttpException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class HttpRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response: Response = await call_next(request)
        except CustomHttpException as ce:
            # カスタム例外
            response = JSONResponse(ce.detail, status_code=ce.status_code)

        return response