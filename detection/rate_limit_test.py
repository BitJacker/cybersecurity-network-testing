import requests
import time

url = input("URL: ")
count = 20

blocked = 0

for i in range(count):
    r = requests.get(url)
    print(f"{i+1} -> {r.status_code}")
    if r.status_code == 429:
        blocked += 1
    time.sleep(0.05)

print("\nRisposte rate‑limited:", blocked)

