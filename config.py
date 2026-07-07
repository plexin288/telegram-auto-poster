import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = int(os.getenv("CHAT_ID", "0"))

    TIMEZONE = os.getenv(
        "TIMEZONE",
        "Asia/Jakarta"
    )

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "database.db"
    )
