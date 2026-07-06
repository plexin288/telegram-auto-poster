from telegram import Bot
from telegram.constants import ParseMode

from config import Config


class TelegramBot:

    def __init__(self):
        self.bot = Bot(token=Config.BOT_TOKEN)

    async def send_text(self, text: str):
        await self.bot.send_message(
            chat_id=Config.CHAT_ID,
            text=text,
            parse_mode=ParseMode.HTML
        )

    async def send_photo(self, photo_path: str, caption: str = ""):
        with open(photo_path, "rb") as photo:
            await self.bot.send_photo(
                chat_id=Config.CHAT_ID,
                photo=photo,
                caption=caption,
                parse_mode=ParseMode.HTML
            )

    async def send_video(self, video_path: str, caption: str = ""):
        with open(video_path, "rb") as video:
            await self.bot.send_video(
                chat_id=Config.CHAT_ID,
                video=video,
                caption=caption,
                parse_mode=ParseMode.HTML
            )
