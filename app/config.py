from pydantic_settings import BaseSettings
from typing import List, Literal

class Settings(BaseSettings):
    # API Keys
    newsapi_key: str = ""
    openai_api_key: str = ""
    gemini_api_key: str = ""
    
    # Provider Selection
    primary_provider: Literal["openai", "gemini", "ollama"] = "openai"
    fallback_providers: List[str] = ["gemini", "ollama"]
    
    # App Settings
    app_name: str = "Las Vegas Times"
    news_country: str = "us"
    news_categories: List[str] = ["general", "business", "entertainment", "politics"]
    
    # Local Model Settings (Ollama)
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "mistral-nemo" # 12B heavy-hitter for Gonzo style
    
    class Config:
        env_file = ".env"

settings = Settings()
