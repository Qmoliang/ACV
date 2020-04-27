# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:07:28 2020

@author: 79167
"""

from PIL import Image
import os
path = "D:\zhaop2\class_name" 
files= os.listdir(path) 
for file in files: 
    if not os.path.isdir(file): 
      img = Image.open(path + "/" + file)
      cropped = img.crop((0, 70, 150, 220))  # (left, upper, right, lower)
      cropped.save(path + "/train/" + file)