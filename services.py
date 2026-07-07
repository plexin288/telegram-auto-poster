from datetime import datetime

from database import SessionLocal
from models import Post
from bot import TelegramBot


class PostService:

    def __init__(self):
        self.bot = TelegramBot()

    async def process_posts(self):

        db = SessionLocal()

        try:

            posts = (
                db.query(Post)
                .filter(Post.is_sent == False)
                .all()
            )

            now = datetime.now()

            for post in posts:

                if post.scheduled_at <= now:

                    if post.type == "text":

                        await self.bot.send_text(
                            post.caption
                        )

                    elif post.type == "photo":

                        await self.bot.send_photo(
                            post.file_path,
                            post.caption
                        )

                    elif post.type == "video":

                        await self.bot.send_video(
                            post.file_path,
                            post.caption
                        )

                    post.is_sent = True

            db.commit()

        finally:
            db.close()
