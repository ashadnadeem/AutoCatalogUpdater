#!/usr/bin/env python3
__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/8/2020"

from PIL import Image
import os

folder = os.path.join(os.path.expanduser("~"),"supplier-data/images")

imgList = os.listdir(folder)

for imgs in imgList:
    if imgs.startswith("."):
        continue
    if imgs.endswith(".tiff"):
        new_ext = imgs.split(".")[0] + ".jpeg"
        im = Image.open(os.path.join(folder,imgs))
        #Convert from RGBA to RGB
        im = im.convert('RGB')
        #Size: Change image resolution from 3000x2000 to 600x400 pixel
        im = im.resize((600,400))
        directory = os.path.join(folder,new_ext)
        new_img = im.save(directory, format="JPEG")
        #remove tiff file
        #os.remove(os.path.join(folder,imgs))