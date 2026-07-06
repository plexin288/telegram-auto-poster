from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import Config
from services import PostService


scheduler = AsyncIOScheduler(
    timezone=Config.TIMEZONE
)

service = PostService()


async def run_scheduler():
    scheduler.add_job(
        service.process_posts,
        "interval",
        seconds=30,
        id="telegram_auto_post"
    )

    scheduler.start()

    print("✅ Scheduler Started (30 seconds)")
