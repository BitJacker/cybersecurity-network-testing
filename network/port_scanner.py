import socket
import os
import sys

# FIX PATH progetto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from core.utils import expand_targets

print("\n=== AUTOMATIC PORT SCANNER ===\n")

target = input("Target (IP o CIDR): ").strip()

targets = expand_targets(target)

# Porte comuni (realistiche)
COMMON_PORTS = [
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    53,   # DNS
    80,   # HTTP
    110,  # POP3
    139,  # SMB
    143,  # IMAP
    443,  # HTTPS
    445,  # SMB
    3306, # MySQL
    3389, # RDP
    8080, # HTTP-alt
]

print(f"\nHost da scansionare: {len(targets)}\n")

for ip in targets:
    print(f"--- {ip} ---")
    found = False

    for port in COMMON_PORTS:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.4)
            s.connect((ip, port))
            print(f"[OPEN] Porta {port}")
            found = True
            s.close()
        except:
            pass

    if not found:
        print("Nessuna porta comune aperta")

    print()

input("Scansione completata. Premi ENTER per uscire")

