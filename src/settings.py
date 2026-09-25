import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()

## if you want to use config file
# in Dockerfile need: "RUN chmod 600 WIREGUARD_SETTINGS_FILE.conf"
# CONFIG_PATH = os.path.abspath("WIREGUARD_SETTINGS_FILE.conf")
# subprocess.run(["wg-quick", "up", CONFIG_PATH], check=True)


@dataclass
class Settings:
    # FTP
    FTP_HOST: str = os.getenv("FTP_HOST", "test_host")
    FTP_USER: str = os.getenv("FTP_USER", "test_user")
    FTP_PASSWORD: str = os.getenv("FTP_PASSWORD", "test_password")

    # RAM file
    INTERFACE_NAME: str = "viper"
    RAM_CONFIG_PATH: str = f"/dev/shm/{INTERFACE_NAME}.conf"

    # wireguard
    wg_config: str = f"""
    [Interface]
    Address = {os.getenv("WG_ADDRESS")}
    PrivateKey = {os.getenv("WG_PRIVATEKEY")}
    ListenPort = {os.getenv("WG_LISTENPORT")}
    DNS = {os.getenv("WG_DNS")}
    
    [Peer]
    PublicKey = {os.getenv("WG_PUBLICKEY")}
    Endpoint = {os.getenv("WG_ENDPOINT")}
    AllowedIPs = {os.getenv("WG_ALLOWEDIPS")}
    PersistentKeepalive = {os.getenv("WG_PERSISTENKEEPALIVE")}
    """

    @staticmethod
    def secure_opener(path, flags):
        """
        Open the file with restrictive permissions (0600),
        readable and writable only by the owner.
        """
        return os.open(path, flags, 0o600)
