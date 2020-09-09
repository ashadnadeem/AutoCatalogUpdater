#! /usr/bin/env python3
__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/8/2020"

import os
import requests

image_folder = os.path.join(os.path.expanduser("~"),"supplier-data/images")
data_folder = os.path.join(os.path.expanduser("~"),"supplier-data/descriptions")

list_image_files = os.listdir(image_folder)
list_images = [image_name for image_name in list_image_files if '.jpeg' in image_name]

list_of_files = os.listdir(data_folder)
url = "http://34.122.42.103/fruits/"
dict = {}
for file in list_of_files:
    if file.startswith("."):
        continue
    with open(os.path.join(data_folder,file),"r") as current_file:
        name = current_file.readline().strip()
        weight = int(current_file.readline().split(" ")[0])
        disc = current_file.readline().strip()
        img_name = file.split(".")[0] + ".jpeg"
        img_path = os.path.join(image_folder, img_name)
        dict = {"name": name,
                "weight": weight,
                "description": disc,
                "image_name": img_path}
        for image_file in list_images:
            if image_file.split('.')[0] in file.split('.')[0]:
                dict['image_name'] = image_file
    response = requests.post(url, json=dict)
    if not response.ok:
        print(response.status_code)
    elif response.status_code == 201:
        print("Status posted Successfully")
