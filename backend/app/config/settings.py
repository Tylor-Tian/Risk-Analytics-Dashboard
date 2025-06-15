from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Risk Analytics Dashboard API"
    environment: str = "development"

    class Config:
        env_file = ".env"
