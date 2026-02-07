import socket
import time
from core.utils import expand_targets

target = input("Target (IP o CIDR): ")
port = int(input("Porta: "))
rate = int(input("Pacchetti/sec: "))
duration = int(input("Durata (sec): "))

targets = expand_targets(target)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = b"NET_TEST"

interval = 1 / rate
end_time = time.time() + duration
sent = 0

print(f"\nTarget totali: {len(targets)}")
print("Avvio test UDP... CTRL+C per fermare\n")

try:
    while time.time() < end_time:
        for ip in targets:
            sock.sendto(payload, (ip, port))
            sent += 1
            time.sleep(interval)
except KeyboardInterrupt:
    pass

print(f"\nPacchetti inviati: {sent}")

