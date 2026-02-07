import socket
import time

host = input("Host: ")
port = 80

s = socket.socket()
s.connect((host, port))

s.send(b"GET / HTTP/1.1\r\n")
time.sleep(2)
s.send(f"Host: {host}\r\n".encode())
time.sleep(2)
s.send(b"\r\n")

print("Slow request inviata")
s.close()

