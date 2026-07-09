from services import PostService

service = PostService()


async def run_scheduler():
    print("Checking scheduled posts...")

    await service.process_posts()

    print("Done.")
