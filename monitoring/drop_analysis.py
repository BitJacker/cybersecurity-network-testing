import subprocess

target = input("Target IP: ")

out = subprocess.getoutput(f"ping -c 20 {target}")
print(out)

if "packet loss" in out:
    print("\nAnalisi perdita pacchetti completata")

