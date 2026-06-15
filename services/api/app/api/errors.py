from http import HTTPStatus

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def error_response(
    code: str,
    message: str,
    status_code: int,
    details: object | None = None,
) -> JSONResponse:
    payload: dict[str, object] = {
        "error": {
            "code": code,
            "message": message,
        }
    }
    if details is not None:
        payload["error"]["details"] = details
    return JSONResponse(status_code=status_code, content=payload)


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return _http_error_response(exc.status_code, exc.detail)


async def starlette_http_exception_handler(
    request: Request,
    exc: StarletteHTTPException,
) -> JSONResponse:
    return _http_error_response(exc.status_code, exc.detail)


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    return error_response(
        code="validation_error",
        message="Request validation failed",
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        details=exc.errors(),
    )


def _http_error_response(status_code: int, detail: object) -> JSONResponse:
    if status_code == HTTPStatus.NOT_FOUND:
        code = "not_found"
    else:
        code = "http_error"

    try:
        message = HTTPStatus(status_code).phrase
    except ValueError:
        message = "HTTP Error"

    if status_code != HTTPStatus.NOT_FOUND and detail:
        message = str(detail)

    return error_response(code=code, message=message, status_code=status_code)
