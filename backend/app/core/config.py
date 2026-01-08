from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    app_name: str = "backend-api"
    api_host: str = "0.0.0.0"
    api_port: int = 8080
    
    postgres_url: str
    mongo_url: str
    mongo_db: str

settings = Settings()
