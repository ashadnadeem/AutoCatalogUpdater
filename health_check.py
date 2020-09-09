#!/usr/bin/env python3
__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/8/2020"

import shutil
import socket
import psutil
import emails

def sendEmail(subject):
    msg = emails.generate_error_report("automation@example.com",
                          "<user>@example.com",
                          subject,
                          "Please check your system and resolve the issue as soon as possible."
                          )
    emails.send(msg)

def checkCondition():
    subject = ""
    du = shutil.disk_usage("/")
    if psutil.cpu_percent(1) > 80:
        subject = "Error - CPU usage is over 80%"

    elif (du.free / du.total * 100) < 20:
        subject = "Error - Available disk space is less than 20%"

    elif psutil.virtual_memory().available/(1024*1024) < 500 :
        subject = "Error - Available memory is less than 500MB"

    elif not check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"

    return subject

def check_localhost():
    localhost = socket.gethostbyname("localhost")
    if (localhost == "127.0.0.1"):
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        subject = checkCondition()
        if subject != "":
            sendEmail(subject)