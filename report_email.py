#!/usr/bin/env python3
__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/8/2020"

from datetime import datetime, date
import os

import emails
import reports

def getfruitlist():
    data_folder = os.path.join(os.path.expanduser("~"), "supplier-data/descriptions")
    list_of_files = os.listdir(data_folder)
    data = ""
    for file in list_of_files:
        if file.startswith("."):
            continue
        with open(os.path.join(data_folder, file), "r") as current_file:
            name = current_file.readline().strip()
            weight = int(current_file.readline().strip())
            data = data + name + "<br/>" + weight + "<br/>" + "<br/>"
    return data

if __name__ == "__main__":
    filename = "processed.pdf"
    title = "Processed Update on {}".format(date.today().strftime("%B %d, %Y"))
    data = getfruitlist()
    reports.generate(filename,title,data)
    msg = emails.generate("automation@example.com",
                          "<user>@example.com",
                          "Upload Completed - Online Fruit Store",
                          "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                          "processed.pdf")
    emails.send(msg)