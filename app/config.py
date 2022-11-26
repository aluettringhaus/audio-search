from pydantic import BaseSettings


class Settings(BaseSettings):
    redis: dict = {
        "host": "localhost",
        "port": 6379,
        "db": 1,
        "decode_responses": True,
    }
    cohere: dict = {
        "api-key": "",
        "model": "large",
        "truncate": "RIGHT",
    }


settings = Settings()
