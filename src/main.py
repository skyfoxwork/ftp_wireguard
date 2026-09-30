import os

from settings import Settings
from services.vpn_wireguard import ping
from services.ftp_manager import csv_downloader


app_settings = Settings()

csv_work_dir = f"{app_settings.CONTAINER_DOWNLOADS_PATH}/csv"

os.makedirs(csv_work_dir, exist_ok=True)

def main() -> None:
    cats = ["814", "817"]

    csv_downloader(cats, csv_work_dir)

if __name__ == "__main__":
    ping()
    main()
