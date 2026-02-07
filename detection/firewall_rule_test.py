import socket

target = input("Target IP: ")
ports = [22, 80, 443]

for p in ports:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((target, p))
        print(f"[APERTO] Porta {p}")
    except:
        print(f"[BLOCCATO] Porta {p}")
    s.close()

