import socket
import time

target = input("Target IP: ")
port = int(input("Porta: "))
max_conn = int(input("Numero connessioni (es. 50): "))

sockets = []

print("\nAvvio test connessioni...\n")

for i in range(max_conn):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        sockets.append(s)
        print(f"[+] Connessione {i+1} OK")
        time.sleep(0.05)  # rate limit
    except Exception as e:
        print(f"[-] Connessione {i+1} fallita")
        break

input("\nTest completato. ENTER per chiudere le connessioni")

for s in sockets:
    s.close()

