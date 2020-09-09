#!/usr/bin/env python3
__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/9/2020"

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
image_folder = os.path.join(os.path.expanduser("~"),"supplier-data/images")
imglist = os.listdir(image_folder)
for imgs in imglist:
    if imgs.endswith(".tiff"):
        continue
    if imgs.startswith("."):
        continue
    with open(os.path.join(image_folder,imgs), 'rb') as opened:
        r = requests.post(url, files={'file': opened})
