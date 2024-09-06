import psutil
from time import sleep
from subprocess import run
from dotenv import dotenv_values
from pyautogui import click
from sys import exit

env = dotenv_values(".env")


def get_current_download_speed():
    network_io_counters = psutil.net_io_counters()
    return network_io_counters.bytes_recv


def reconnect_wifi():
    run(["netsh", "wlan", "disconnect"])
    run(["netsh", "wlan", "connect", f"{env['WIFI']}"])


def close_browser():
    click(1895, 22)
    exit("Stopping browser")


def main():
    last_total_bytes = 0
    print("Press CTRL+C to exit")
    above_threshold_count = 0
    while True:
        current_bytes = get_current_download_speed()
        download_speed = current_bytes - last_total_bytes
        download_speed_mbps = download_speed / 1024 / 1024
        last_total_bytes = current_bytes

        print(f"Download Speed: {download_speed_mbps:.2f} Mbps")
        if download_speed_mbps < 0.03:
            print("Not fully connected, skipping....")
        else:
            if download_speed_mbps < 19:
                print("Reconnecting to WiFi...")
                reconnect_wifi()
                above_threshold_count = 0
            else:
                above_threshold_count += 1
                if above_threshold_count >= 7:
                    print("Closing the browser...")
                    close_browser()
                    break

        # time in seconds before it checks the download speed again
        sleep(int(env['TIME']))


if __name__ == "__main__":
    main()
