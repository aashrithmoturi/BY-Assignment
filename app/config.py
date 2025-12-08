from pydantic_settings import BaseSettings

# BaseSettings is for loading config data from env variables
class Settings(BaseSettings):
    database_url: str
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()