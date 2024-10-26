from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    """
    Configuration settings for the application.
    """

    llm_api_key: str = Field(env="LLM_API_KEY")
    debug_mode: bool = Field(default=False, env="DEBUG_MODE")
    log_level: str = Field(default="INFO", env="LOG_LEVEL") 

    class Config:
        env_file = ".env" 

config = Config()