import os
import sys
import subprocess

class Colors:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    END = "\033[0m"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MENU = {
    "1": ("Connection Exhaustion", "network/conn_exhaustion.py"),
    "2": ("MTU Test", "network/mtu_test.py"),
    "3": ("Fragmentation Test", "network/fragmentation_test.py"),
    "4": ("HTTP Stress Test", "application/http_stress.py"),
    "5": ("Slow HTTP Test", "application/slow_http.py"),
    "6": ("DNS Load Test", "application/dns_load.py"),
    "7": ("IDS Trigger Test", "detection/ids_trigger_test.py"),
    "8": ("Rate Limit Test", "detection/rate_limit_test.py"),
    "9": ("Latency Monitor", "monitoring/latency_monitor.py"),
    "10": ("Port Scanner", "network/port_scanner.py"),
    "0": ("Exit", None)
}

def clear():
    os.system("clear")

def run_script(rel_path):
    full_path = os.path.join(BASE_DIR, rel_path)

    if not os.path.isfile(full_path):
        input(f"{Colors.RED}[ERRORE] File non trovato: {rel_path}{Colors.END}\nPremi ENTER per tornare al menu")
        return

    # Comando universale per aprire nuovo terminale e restare in attesa
    cmd = f'bash -c "python3 \\"{full_path}\\"; echo; read -p \'Premi ENTER per chiudere\'"'

    try:
        subprocess.Popen(["xfce4-terminal", "--hold", "--command", cmd])
    except FileNotFoundError:
        # fallback se xfce4-terminal non c'è
        os.system(f"python3 {full_path}")
        input("\nPremi ENTER per tornare al menu")

def main():
    while True:
        clear()
        print(f"{Colors.BLUE}{'='*50}{Colors.END}")
        print(f"{Colors.YELLOW}{'Created by BitJacker':^50}{Colors.END}")
        print(f"{Colors.CYAN}{'Cybersecurity Network Testing Lab':^50}{Colors.END}")
        print(f"{Colors.BLUE}{'='*50}{Colors.END}\n")

        for key, value in MENU.items():
            print(f"{Colors.GREEN}{key}. {value[0]}{Colors.END}")

        choice = input(f"\n{Colors.YELLOW}Seleziona un'opzione > {Colors.END}").strip()

        if choice == "0":
            print(f"{Colors.BLUE}Uscita...{Colors.END}")
            sys.exit(0)

        elif choice in MENU:
            run_script(MENU[choice][1])

        else:
            input(f"{Colors.RED}Scelta non valida. PREMI ENTER per riprovare{Colors.END}")

if __name__ == "__main__":
    main()

