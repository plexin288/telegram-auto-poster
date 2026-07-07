from datetime import datetime

from database import init_db
from models import add_post


def main():

    init_db()

    print("=" * 40)
    print("TELEGRAM AUTO POSTER")
    print("=" * 40)

    print("\nPilih jenis postingan")
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

    text = input("Caption / Text: ").strip()

    schedule_time = input(
        "Jadwal (YYYY-MM-DD HH:MM:SS): "
    ).strip()

    try:
        datetime.strptime(
            schedule_time,
            "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        print("Format tanggal salah.")
        return

    add_post(
        post_type=post_type,
        text=text,
        file_path=file_path,
        schedule_time=schedule_time
    )

    print("\n✅ Post berhasil ditambahkan.")


if __name__ == "__main__":
    main()
