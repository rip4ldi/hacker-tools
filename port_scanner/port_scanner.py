# ================================================================================
# FILE NAME:  port_scanner.py
#
# PURPOSE:
# A simple port scanner. Very slow, but it works.
#
# CREATED DATE: 2021-09-19
# AUTHOR:       @hedgenull
# ================================================================================

# Import libraries
import socket
from colorama import Fore, init

init()

# Colors
GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

# Server to scan
host = input(f"{GREEN}Server to scan: ")
print(RESET)
ip = socket.gethostbyname(host)

# Setup
MAX_PORTS = 65535   # Stop after port 65535
port_num = 1    # Start at port 1

# File setup
file_name = f"open_ports\ports_{ip}.txt"
file = open(file_name, "w")
file_content = f"Open ports at server {ip}:\n"


# Main loop
for port in range(port_num, MAX_PORTS):   # Stop after port 65535
    try:
        s = socket.socket()     # Connect to the port
        r = s.connect((ip, port))
        print(f"{GREEN}Port {port} is open!{RESET}")    # If connection succeeds, port is open
        file_content += f"{port} is open.\n"
    except:
        print(f"{GRAY}Port {port} is closed.{RESET}")   # If connection fails, port is closed
    port += 1

file.write(file_content)