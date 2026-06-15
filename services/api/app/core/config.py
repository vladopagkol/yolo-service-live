from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Object Detection API"
    app_version: str = "0.1.0"
    environment: str = "development"

    model_config = SettingsConfigDict(env_prefix="API_", extra="ignore")


settings = Settings()

