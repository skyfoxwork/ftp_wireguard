from ftplib import FTP_TLS

from src import app_settings
from vpn_wireguard import wireguard, ping


@wireguard
def main():
    with FTP_TLS(app_settings.FTP_HOST) as ftp:

        ftp.auth()

        ftp.login(user=app_settings.FTP_USER, passwd=app_settings.FTP_PASSWORD)

        ftp.prot_p()

        print(ftp.getwelcome())

        ftp.retrlines('LIST')

if __name__ == "__main__":
    ping()
    main()
