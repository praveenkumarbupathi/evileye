import subprocess
import time
import requests
from config import NGROK_PORT

class NgrokTunnel:
    def __init__(self):
        self.ngrok_url = None

    def start(self):
        print("[+] Starting Ngrok tunnel...")
        subprocess.Popen(['ngrok', 'http', str(NGROK_PORT)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)  # Allow Ngrok time to initialize
        self.fetch_url()

    def fetch_url(self):
        try:
            response = requests.get("http://127.0.0.1:4040/api/tunnels")
            tunnel_info = response.json()
            self.ngrok_url = tunnel_info['tunnels'][0]['public_url']
            print(f"[✓] Ngrok URL: {self.ngrok_url}")
        except requests.RequestException as e:
            print(f"[-] Failed to fetch Ngrok URL: {e}")
            exit()
