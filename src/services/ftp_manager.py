import os
from ftplib import FTP_TLS

from settings import Settings
from services.vpn_wireguard import wireguard


app_settings = Settings()

@wireguard
def csv_downloader(cats_to_download: list[str], download_dir: str) -> None:
    # 1. Connect to the FTP server
    with FTP_TLS(app_settings.FTP_HOST) as ftp:
        # 2. Log in
        ftp.login(user=app_settings.FTP_USER, passwd=app_settings.FTP_PASSWORD)
        # 3. Secure the data connection (required for FTPS after login)
        ftp.prot_p()
        # 4. Print the server's welcome message
        print(ftp.getwelcome())

        # 5. Download files
        for cat in cats_to_download:
            # 1. Move to cat directory
            print(f"\tOpen cat {cat}")
            ftp.cwd(f"{cat}/tmp")
            # 2. List the contents of the current directory
            print("Files in tmp directory:")
            print("=========================================")
            ftp.retrlines("LIST")
            print("=========================================")
            # 3. Download files
            files_to_download = [f"{cat}_filenames.csv", f"{cat}_urls.csv"]

            for filename in files_to_download:
                print(f"Downloading {filename}")
                local_path = os.path.join(download_dir, filename)
                try:
                    with open(local_path, 'wb') as local_file:
                        ftp.retrbinary(f'RETR {filename}', local_file.write)
                    print(f'Download done: {local_path}')
                except Exception as e:
                    print(f"Can`t download {filename}. \nError: {e}")

            # 4. Move to root directory
            ftp.cwd('/')
