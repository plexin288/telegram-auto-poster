from datetime import datetime

from database import SessionLocal, init_db
from models import Post


def main():
    init_db()

    db = SessionLocal()

    print("=" * 40)
    print("TELEGRAM AUTO POSTER")
    print("=" * 40)

    print("\nPilih jenis postingan:")
    print("1. Text")
    print("2. Photo")
    print("3. Video")

    choice = input("\nPilih (1/2/3): ").strip()

    if choice == "1":
        post_type = "text"
        file_path = None

    elif choice == "2":
        post_type = "photo"
        file_path = input("Lokasi foto: ").strip()

    elif choice == "3":
        post_type = "video"
        file_path = input("Lokasi video: ").strip()

    else:
        print("Pilihan tidak valid.")
        return

    caption = input("Caption: ")

    schedule = input(
        "Jadwal (YYYY-MM-DD HH:MM:SS): "
    )

    scheduled_at = datetime.strptime(
        schedule,
        "%Y-%m-%d %H:%M:%S"
    )

    post = Post(
        type=post_type,
        file_path=file_path,
        caption=caption,
        scheduled_at=scheduled_at
    )

    db.add(post)
    db.commit()

    print("\n✅ Post berhasil ditambahkan!")

    db.close()


if __name__ == "__main__":
    main()
