import ssl
import socket

host = input("Host: ")
port = 443

context = ssl.create_default_context()

try:
    with socket.create_connection((host, port), timeout=3) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print("TLS handshake OK")
            print("Protocollo:", ssock.version())
except Exception as e:
    print("Errore TLS:", e)

