import os
import subprocess
from collections.abc import Callable

from settings import Settings


app_settings = Settings()

def vpn_up(config) -> None:
    print("[Python] up VPN...")
    subprocess.run(["wg-quick", "up", config], check=True)

def vpn_down(config) -> None:
    print("[Python] down VPN...")
    subprocess.run(["wg-quick", "down", config], check=True)

def wireguard(funk) -> Callable[[], None]:
    """
    Decorator to automatically turn on and turn off a WireGuard VPN tunnel.

    It creates a temporary configuration file, brings the WireGuard interface UP,
    executes the decorated function inside the secure network tunnel, and
    guarantees that the interface is brought DOWN and the config is deleted
    afterward.
    """
    def wrapper():
        vpn_started = False

        try:
            with open(app_settings.RAM_CONFIG_PATH, "w", opener=app_settings.secure_opener) as f:
                f.write(app_settings.wg_config)

            vpn_up(app_settings.RAM_CONFIG_PATH)
            vpn_started = True
            funk()

        finally:
            if vpn_started:
                vpn_down(app_settings.RAM_CONFIG_PATH)

            if os.path.exists(app_settings.RAM_CONFIG_PATH):
                os.remove(app_settings.RAM_CONFIG_PATH)

    return wrapper

@wireguard
def ping_wg() -> None:
    """
    Test ping function.
    Turn on VPN, send 5 ICMP echo requests to the FTP host, and turn off VPN.
    """
    subprocess.run(["ping", "-c5", app_settings.FTP_HOST], check=True)

def ping(wg: bool = True) -> None:
    """
    Test ping function.
    """
    if wg:
        ping_wg()
    else:
        subprocess.run(["ping", "-c5", app_settings.FTP_HOST], check=True)
