import subprocess
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def launch(script_path):
    full = os.path.join(BASE_DIR, script_path)
    if not os.path.exists(full):
        print("[ERRORE] Script non trovato")
        return

    subprocess.run(["python3", full])

