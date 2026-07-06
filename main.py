import asyncio

from database import init_db
from scheduler import run_scheduler


async def main():

    print("=" * 40)
    print("🚀 Telegram Auto Poster Started")
    print("=" * 40)

    init_db()

    await run_scheduler()

    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
