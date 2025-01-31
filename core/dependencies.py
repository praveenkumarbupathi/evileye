import subprocess

class DependencyChecker:
    def __init__(self):
        self.required_pkgs = ['python3', 'pip3', 'php', 'ssh', 'ngrok']

    def check(self):
        print("[+] Checking Dependencies...")
        missing = []
        for pkg in self.required_pkgs:
            if not self.is_installed(pkg):
                missing.append(pkg)
        
        if missing:
            print(f"[-] Missing dependencies: {', '.join(missing)}")
            print("[!] Please install them before proceeding.")
            exit()
        else:
            print("[✓] All dependencies installed.")

    @staticmethod
    def is_installed(pkg):
        return subprocess.call(["which", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
