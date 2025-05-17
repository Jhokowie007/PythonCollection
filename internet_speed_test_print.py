from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import speedtest
import time
from tqdm import tqdm

class SpeedTestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        st = speedtest.Speedtest()
        for _ in tqdm(range(100), desc="Fetching best server", ncols=70):
            time.sleep(0.005)
        st.get_best_server()

        print("Measuring download speed...")
        download = st.download() / 8_000_000
        print(f"Download: {download:.2f} MBps")

        print("Measuring upload speed...")
        upload = st.upload() / 8_000_000
        print(f"Upload: {upload:.2f} MBps")

        ping = st.results.ping
        print(f"Ping: {ping:.2f} ms")

        layout.add_widget(Label(text=f"Download: {download:.2f} MBps"))
        layout.add_widget(Label(text=f"Upload: {upload:.2f} MBps"))
        layout.add_widget(Label(text=f"Ping: {ping:.2f} ms"))
        return layout

if __name__ == '__main__':
    SpeedTestApp().run()
