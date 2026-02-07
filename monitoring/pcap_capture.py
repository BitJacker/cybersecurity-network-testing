import os

iface = input("Interfaccia: ")
file = input("File pcap: ")

print("CTRL+C per fermare")
os.system(f"sudo tcpdump -i {iface} -w {file}")

