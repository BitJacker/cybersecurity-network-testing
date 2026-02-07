import os
import sys
import requests

# aggiunge la root del progetto al PYTHONPATH
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

def main():
    url = input("Target URL (es. http://httpbin.org/get): ").strip()
    count = int(input("Numero richieste (es. 5): "))

    print("\n[+] Avvio HTTP stress test\n")

    for i in range(1, count + 1):
        try:
            r = requests.get(url, timeout=5)
            print(f"[{i}] Status: {r.status_code}")
        except Exception as e:
            print(f"[{i}] ERRORE: {e}")

    input("\nPremi ENTER per tornare al menu")

if __name__ == "__main__":
    main()

