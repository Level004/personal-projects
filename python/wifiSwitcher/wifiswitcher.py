import psutil
from time import sleep
from subprocess import run
from dotenv import dotenv_values

env = dotenv_values(".env")


def get_current_download_speed():
    # Get current network usage in bytes per second
    network_io_counters = psutil.net_io_counters()
    return network_io_counters.bytes_recv


def reconnect_wifi():
    # Below command is for Windows, change it for other platforms.
    run(["netsh", "wlan", "disconnect"])
    run(["netsh", "wlan", "connect", f"{env['WIFI']}"])


def main():
    last_total_bytes = 0
    print("Press CTRL+C to exit")
    while True:
        current_bytes = get_current_download_speed()
        download_speed = current_bytes - last_total_bytes
        last_total_bytes = current_bytes

        print(f"Download Speed: {download_speed / 1024 / 1024:.2f} Mbps")

        if download_speed == 0:
            print("Reconnecting to WiFi...")
            reconnect_wifi()

        # time in seconds before it checks the download speed again
        sleep(int(env['TIME']))


if __name__ == "__main__":
    main()
