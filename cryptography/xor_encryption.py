# ================================================================================
# FILE NAME:  xor_encryption.py
#
# PURPOSE:
# Encrypt a string with the one-time pad algorithm (XOR)
#
# CREATED DATE: 2022-02-24
# AUTHOR:       @hedgenull
# ================================================================================

import random

def generate_key(length):
    CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]{};:,.<>/?|`~"

    key = ""
    for i in range(length):
        key += random.choice(CHARSET)
    
    return key

def xor_encryption(key, value):
    return "".join([hex(ord(key[i%len(key)]) ^ ord(value[i%len(value)]))[2:] for i in range(max(len(key), len(value)))])

if __name__ == "__main__":
    string = input("Enter message to be encrypted: ")
    key = generate_key(len(string))
    encrypted = xor_encryption(key, string)
    print("KEY: %s" % key)
    print("ENCRYPTED STRING: %s" % encrypted)