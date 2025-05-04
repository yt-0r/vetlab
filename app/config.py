from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Lab Results Service"
    host: str = "127.0.0.1"
    port: int = 8090
    database_url: str = "sqlite:///./lab_results.db"

    class Config:
        env_file = "../.env"


settings = Settings()
