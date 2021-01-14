#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 08:40:46 2020

@author: vishnu
"""

import time

import cv2
import pytesseract


img = cv2.imread('/home/vishnu/Downloads/Workouts ML/02.Deep Learning/Optical Character Recognition/data/novel.jpeg') #reading image
start = time.time()
print("Text extracted using Tesseract\n")
print(pytesseract.image_to_string(img))
end = time.time()
t = end-start
print("\nTime Taken   ", t, " (s)")