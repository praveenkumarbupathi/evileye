import subprocess
import time
from config import NGROK_PORT, TEMPLATES_DIR

class WebServer:
    def __init__(self):
        self.port = NGROK_PORT

    def start(self):
        print(f"[+] Starting PHP server on port {self.port}...")
        subprocess.Popen(['php', '-S', f'0.0.0.0:{self.port}', '-t', TEMPLATES_DIR], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)
        print("[✓] Web server started successfully.")
