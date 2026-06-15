from fastapi import FastAPI

from app.api.routes import router as health_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(health_router, prefix="/api/v1")


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok"}
