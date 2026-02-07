from datetime import datetime
import os

os.makedirs("reports", exist_ok=True)

name = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(name, "w") as f:
    f.write("Cybersecurity Network Testing Report\n")
    f.write(f"Data: {datetime.now()}\n")
    f.write("Test completati manualmente\n")

print("Report generato:", name)

