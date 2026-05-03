import os

from dotenv import load_dotenv

load_dotenv()

BASE_HOST: str | None = os.getenv("BASE_API_HOST")
API_MODULE: str = os.getenv("API_MODULE", "/api")
API_TOKEN: str | None = os.getenv("API_TOKEN")
APP_URL: str = f"{os.getenv('APP_URL')}/?user-id={API_TOKEN}"

LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
