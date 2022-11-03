import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_NAME = os.getenv("APP_NAME")
    LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL", "DEBUG")
    IS_MONITOR_BY_TELEGRAM: int = int(os.getenv("IS_MONITOR_BY_TELEGRAM", 0))
    MONITOR_BOT_ID = os.getenv("MONITOR_BOT_ID")
    MONITOR_CHAT_ID = os.getenv("MONITOR_CHAT_ID")
