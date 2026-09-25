import os
import subprocess

from src import app_settings


def vpn_up(config):
    print("[Python] up VPN...")
    subprocess.run(["wg-quick", "up", config], check=True)

def vpn_down(config):
    print("[Python] down VPN...")
    subprocess.run(["wg-quick", "down", config], check=True)

def wireguard(funk):
    """
    Decorator to automatically turn on and turn off a WireGuard VPN tunnel.

    It creates a temporary configuration file, brings the WireGuard interface UP,
    executes the decorated function inside the secure network tunnel, and
    guarantees that the interface is brought DOWN and the config is deleted
    afterward.
    """
    def wrapper():
        try:
            with open(app_settings.RAM_CONFIG_PATH, "w", opener=app_settings.secure_opener) as f:
                f.write(app_settings.wg_config)

            vpn_up(app_settings.RAM_CONFIG_PATH)
            funk()
            vpn_down(app_settings.RAM_CONFIG_PATH)

        finally:
            if os.path.exists(app_settings.RAM_CONFIG_PATH):
                os.remove(app_settings.RAM_CONFIG_PATH)

    return wrapper

@wireguard
def ping():
    """
    Test ping function.
    Turn on VPN, send 5 ICMP echo requests to the FTP host, and turn off VPN.
    """
    subprocess.run(["ping", "-c5", app_settings.FTP_HOST], check=True)
