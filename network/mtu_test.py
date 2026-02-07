import subprocess
import sys

def mtu_test():
    target = input("Target IP (es. 8.8.8.8): ").strip()

    print("\n[+] Avvio MTU discovery test\n")

    max_ok = None

    for size in range(1200, 1501, 10):
        cmd = ["ping", "-c", "1", "-M", "do", "-s", str(size), target]

        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=2
            )

            if result.returncode == 0:
                print(f"[OK]   Payload {size}")
                max_ok = size
            else:
                print(f"[FAIL] Payload {size} → MTU superata")
                break

        except subprocess.TimeoutExpired:
            print(f"[TIMEOUT] Payload {size}")
            break

    print("\n==============================")
    if max_ok:
        print(f"[✓] MTU massima stabile: {max_ok + 28} byte")
        print(f"[✓] Payload massimo: {max_ok}")
    else:
        print("[!] Nessun valore MTU valido trovato")
    print("==============================")

    input("\nPremi ENTER per tornare al menu")

if __name__ == "__main__":
    mtu_test()

