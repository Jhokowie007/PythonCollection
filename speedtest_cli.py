import subprocess
import sys

# Fungsi untuk memeriksa dan menginstal pustaka speedtest-cli
def install_speedtest():
    try:
        # Menginstal pustaka speedtest-cli
        subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])
    except Exception as e:
        print(f"Gagal menginstal speedtest-cli: {e}")
        sys.exit(1)

# Memeriksa keberadaan pustaka speedtest-cli
try:
    import speedtest
except ImportError:
    print("Pustaka speedtest-cli tidak ditemukan. Menginstal...")
    install_speedtest()
    print("Instalasi selesai. Memeriksa kembali...")
    import speedtest  # Mengimpor kembali setelah instalasi

def cek_kecepatan_internet():
    # Membuat objek Speedtest
    st = speedtest.Speedtest()

    # Mengambil daftar server
    print("Mengambil daftar server...")
    st.get_best_server()

    # Mengukur kecepatan unduh
    print("Mengukur kecepatan unduh...")
    unduh = st.download()  # kecepatan unduh dalam bit per detik

    # Mengukur kecepatan unggah
    print("Mengukur kecepatan unggah...")
    unggah = st.upload()  # kecepatan unggah dalam bit per detik

    # Mengukur ping
    print("Mengukur ping...")
    ping = st.results.ping  # waktu ping dalam ms

    # Mengkonversi kecepatan dari bit per detik ke megabyte per detik
    unduh_MBps = unduh / 8_000_000  # konversi ke MBps
    unggah_MBps = unggah / 8_000_000  # konversi ke MBps

    # Menampilkan hasil
    print(f"Kecepatan Unduh: {unduh_MBps:.2f} MBps")
    print(f"Kecepatan Unggah: {unggah_MBps:.2f} MBps")
    print(f"Ping: {ping:.2f} ms")
    
    # Memberikan input enter untuk keluar program
    input("\n\nPress the enter key to exit : ")

# Memanggil fungsi untuk mengecek kecepatan internet
if __name__ == "__main__":
    cek_kecepatan_internet()
else:
    input("it looks like you're not running it as a main program...\n\nPress the enter key to exit...")
