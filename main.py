import asyncio

from database import init_db
from scheduler import run_scheduler


async def main():
    print("=" * 40)
    print("🚀 Telegram Auto Poster Started")
    print("=" * 40)

    # Inisialisasi database
    init_db()

    # Jalankan scheduler SATU KALI
    await run_scheduler()

    print("✅ Scheduler selesai.")


if __name__ == "__main__":
    asyncio.run(main())
