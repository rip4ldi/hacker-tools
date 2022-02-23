# ================================================================================
# FILE NAME:  crypto.py
#
# PURPOSE:
# Encrypt and decrypt files
#
# CREATED DATE: 2021-09-18
# AUTHOR:        @hedgenull, Abdou Rockikz (thepythoncode.com)
# ================================================================================

# Import libraries
from os import read
from cryptography.fernet import Fernet


def write_key():
    """
    Generates a key and saves it to a file.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named 'key.key'
    """
    return open("key.key", "rb").read()


def encrypt(filename: str, key: bytes):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    f = Fernet(key)

    with open(filename, "rb") as file:
        # Read file data
        file_data = file.read()

        # Encrypt the data
        encrypted_data = f.encrypt(file_data)

    # Write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename: str, key: bytes):
    """
    Given a filename (str) and key (bytes), it decrypts the file and writes it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # Read the encrypted data
        encrypted_data = file.read()
    # Decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # Write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


write_key()
key = load_key()
print(key)