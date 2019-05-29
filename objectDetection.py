# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:59:14 2019

@author: Deepankar
"""

import cv2
import matplotlib as plt
import numpy as np

initial_image = cv2.imread('IMG_20190528_212944.jpg')
gray_image = cv2.cvtColor(initial_image, cv2.COLOR_BGR2GRAY)
median_image = cv2.medianBlur(gray_image, 3)


height = len(median_image)
flag_for_separation=0
line_index = []
j=0
lines = []

#plt.pyplot.imshow(sharpened)

for i in range(height):
    if median_image[i][10]==0 and flag_for_separation==0:
        line_index.append(i)
        flag_for_separation=1
    if flag_for_separation==1:
        j+=1
        if j==6:
            j=0
            flag_for_separation=0
        

for i in range(len(line_index)-1):
    start=line_index[i]
    stop=line_index[i+1]
    temp=[]
    for j in range(start,stop):
        temp.append(median_image[j])
    lines.append(temp)
    
plt.pyplot.imshow(lines[2])    