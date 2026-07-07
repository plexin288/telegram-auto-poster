from datetime import datetime

from models import (
    get_pending_posts,
    mark_sent
)

from bot import TelegramBot


class PostService:

    def __init__(self):
        self.bot = TelegramBot()

    async def process_posts(self):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        posts = get_pending_posts(now)

        for post in posts:

            if post["type"] == "text":

                await self.bot.send_text(
                    post["text"]
                )

            elif post["type"] == "photo":

                await self.bot.send_photo(
                    post["file_path"],
                    post["text"]
                )

            elif post["type"] == "video":

                await self.bot.send_video(
                    post["file_path"],
                    post["text"]
                )

            mark_sent(post["id"])

        if posts:
            print(f"✅ {len(posts)} post berhasil dikirim.")
