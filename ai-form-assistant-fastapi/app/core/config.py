from urllib.parse import quote_plus
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str
    HOST: str
    PORT: int
    DEBUG: bool

    JWT_SECRET: str
    
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_DRIVER: str = "postgresql+psycopg"

    OPENAI_API_KEY: str = ""

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DB_DRIVER}://{quote_plus(self.DB_USER)}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()