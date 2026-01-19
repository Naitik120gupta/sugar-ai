"""
Configuration settings for Sugar-AI.
"""
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Dict, List, Any, Optional

class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Dev mode (THIS MUST EXIST)
    DEV_MODE: bool = os.getenv("DEV_MODE", "0") == "1"

    API_KEYS: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    MODEL_CHANGE_PASSWORD: str = ""
    DEFAULT_MODEL: str = "Qwen/Qwen2-1.5B-Instruct"
    DOC_PATHS: List[str] = Field(default_factory=list)
    MAX_DAILY_REQUESTS: int = 100

    github_client_id: Optional[str] = None
    github_client_secret: Optional[str] = None
    google_client_id: Optional[str] = None
    google_client_secret: Optional[str] = None
    oauth_redirect_uri: Optional[str] = None
    session_secret_key: Optional[str] = None

    port: int = 8000
    TEMPLATES_DIR: str = "templates"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )

settings = Settings()
