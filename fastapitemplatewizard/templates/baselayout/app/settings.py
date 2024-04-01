from pydantic_settings import BaseSettings
from functools import lru_cache


@lru_cache()
class Settings(BaseSettings):
    app_name:   str
    debug:      bool = True


settings = Settings()
