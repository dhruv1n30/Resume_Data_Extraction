from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    APP_NAME: str = "Resume Extractor"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
