import os, threading, queue

def decrypt(key):
    while True:
        file = q.get()
        print(f"Decrypting {file}")
        try: