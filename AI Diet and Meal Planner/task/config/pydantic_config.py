from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the path to project's root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


# Add to handle the environment variables(API_KEY) in both local and docker environments
class Settings(BaseSettings):
    groq_api_key: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
