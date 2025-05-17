from typing import List
import platform
import subprocess
import sys
import time

libs_requirement: List[str] = ["speedtest", "tqdm"]


def install_libs(lib_name:str):
    """Attempting to install the necessary library before continue"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib_name])
    except Exception as e:
        print(f'Failed to install {lib_name}: {e}')
        sys.exit(1)


def clear_console():
    """Attempt to clear console screen"""
    try:
        # if os.name == "Windows": os.system('cls')
        # else: os.system('clear')
        command = 'cls' if platform.system() == "Windows" else "clear"
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(f'Failed to clear the console: {e}')


def main():
    """Attempt to import lib and measuring internet speed"""
    for lib_name in libs_requirement:
        try:
            subprocess.run([sys.executable, "-c", f"import {lib_name.split('-')[0]}"], check=True)
        except subprocess.CalledProcessError:
            print(f"{lib_name} not found, start installing")
            install_libs(lib_name)
            print(f"installation {lib_name} done. re-Check....")
            subprocess.run([sys.executable, "-c", f"import {lib_name}"], check=True)

    import speedtest
    from tqdm import tqdm

    st = speedtest.Speedtest()

    print("Fetching best server...")
    st.get_best_server()
    tqdm(range(100), desc="Done", ncols=70, leave=False)
    time.sleep(0.1)

    print("Measuring download speed...")
    download = st.download() / 1_000_000
    tqdm(range(100), desc="Done", ncols=70, leave=False)
    time.sleep(0.1)
    print(f'Download speed: {download / 8:.2f} MBps / {download:.2f} Mbps\n')

    print("Measuring upload speed...")
    upload = st.upload() / 1_000_000
    tqdm(range(100), desc="Done", ncols=70, leave=False)
    time.sleep(0.1)
    print(f'Upload speed: {upload / 8:.2f} MBps / {upload:.2f} Mbps\n')

    ping = st.results.ping
    tqdm(range(100), desc="Measuring ping", ncols=70, leave=False)
    time.sleep(0.1)
    print(f'Ping: {ping / 1_000:.2f} s / {ping:.2f} ms\n')

    input("press the enter key to exit the program:")


if __name__ == "__main__":
    clear_console()
    main()
else:
    input("it looks like you're not running it as a main program...\n\nPress the enter key to exit...")