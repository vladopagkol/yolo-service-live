from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient
from fastapi import HTTPException
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.errors import (
    http_exception_handler,
    starlette_http_exception_handler,
    validation_exception_handler,
)
from app.main import app as production_app


def test_unknown_route_returns_standard_not_found() -> None:
    client = TestClient(production_app)

    response = client.get("/missing-route")

    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "not_found",
            "message": "Not Found",
        }
    }


class Payload(BaseModel):
    name: str


def test_validation_error_returns_standard_shape() -> None:
    test_app = FastAPI(
        exception_handlers={
            HTTPException: http_exception_handler,
            StarletteHTTPException: starlette_http_exception_handler,
            RequestValidationError: validation_exception_handler,
        }
    )

    @test_app.post("/items")
    def create_item(payload: Payload) -> dict[str, str]:
        return {"name": payload.name}

    client = TestClient(test_app)

    response = client.post("/items", json={})

    assert response.status_code == 422
    body = response.json()
    assert body["error"]["code"] == "validation_error"
    assert body["error"]["message"] == "Request validation failed"
    assert "details" in body["error"]
