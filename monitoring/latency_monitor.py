import subprocess
import statistics

target = input("Target IP: ")

out = subprocess.getoutput(f"ping -c 10 {target}")
print(out)

times = []
for line in out.splitlines():
    if "time=" in line:
        t = float(line.split("time=")[1].split(" ")[0])
        times.append(t)

if times:
    print("\nMedia:", statistics.mean(times), "ms")
    print("Jitter:", statistics.stdev(times), "ms")

