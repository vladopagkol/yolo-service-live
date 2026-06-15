from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.errors import (
    http_exception_handler,
    starlette_http_exception_handler,
    validation_exception_handler,
)
from app.api.routes.health import router as health_router
from app.api.routes.models import router as models_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(health_router, prefix="/api/v1")
app.include_router(models_router, prefix="/api/v1")
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(StarletteHTTPException, starlette_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok"}
