import subprocess
import sys

def main():
    target = input("Target IP (es. 8.8.8.8): ").strip()

    print("\n[+] Invio pacchetti grandi (test frammentazione)\n")

    try:
        # -M do  = non frammentare
        # -s 3000 = payload grande
        cmd = ["ping", "-c", "1", "-M", "do", "-s", "3000", target]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print("[✓] Il pacchetto è passato (frammentazione CONSENTITA)\n")
            print(result.stdout)
        else:
            print("[!] Pacchetto bloccato (frammentazione BLOCCATA)\n")
            print(result.stderr or result.stdout)

    except Exception as e:
        print(f"[ERRORE] {e}")

    input("\nPremi ENTER per tornare al menu")

if __name__ == "__main__":
    main()

