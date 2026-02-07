import socket
import time
from core.utils import expand_targets

target = input("Target (IP o CIDR): ")
port = int(input("Porta: "))
connections = int(input("Connessioni per host: "))

targets = expand_targets(target)

ok = 0
fail = 0

print(f"\nTarget totali: {len(targets)}")

for ip in targets:
    print(f"\nTest su {ip}")
    for _ in range(connections):
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, port))
            ok += 1
            s.close()
        except:
            fail += 1
        time.sleep(0.1)

print("\nRISULTATO")
print("Connessioni OK:", ok)
print("Connessioni FAIL:", fail)

