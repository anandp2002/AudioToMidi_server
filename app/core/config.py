from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MP3 to MIDI Converter"
    API_V1_STR: str = "/api/v1"
    
    # CORS Configuration
    BACKEND_CORS_ORIGINS: list = ["*"]  # In production, replace with specific origins

    class Config:
        case_sensitive = True

settings = Settings()
