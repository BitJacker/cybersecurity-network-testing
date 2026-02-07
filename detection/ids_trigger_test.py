patterns = ["DROP", "BLOCK", "DENY"]

logfile = input("Path file log IDS: ")

with open(logfile) as f:
    lines = f.readlines()

hits = [l for l in lines if any(p in l for p in patterns)]

print("\nEventi sospetti trovati:", len(hits))
for h in hits[:5]:
    print(h.strip())

