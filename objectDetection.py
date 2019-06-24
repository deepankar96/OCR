# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:59:14 2019

@author: Deepankar
"""

import cv2
import matplotlib as plt
import numpy as np
import math

initial_image = cv2.imread('img-1.jpg')
'''kernel = np.ones((5,5),np.uint8)
morph1 = cv2.erode(initial_image,kernel,iterations = 1)
gray_image = cv2.cvtColor(morph1, cv2.COLOR_BGR2GRAY)
median_image = cv2.medianBlur(gray_image, 3)
'''


def image_smoothening(img):
    ret1, th1 = cv2.threshold(img,127, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th2, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th3
def remove_noise_and_smooth(file_name):
    im = cv2.imread(file_name, 0)
    kernel1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(im, -1, kernel1)
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    img = image_smoothening(img)
    or_image = cv2.bitwise_or(img, closing)
    return or_image

median_image = remove_noise_and_smooth('img-1.jpg')




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
        if j==11:
            j=0
            flag_for_separation=0
        

for i in range(len(line_index)-1):
    start=line_index[i]
    stop=line_index[i+1]
    temp=[]
    for j in range(start+10,stop+40):
        temp.append(median_image[j])
    lines.append(temp)
    
words = []
word_index = []
j=0
flag=0
check = 0

for i in range(len(lines)):
    line_length = len(lines[i])
    check1 = math.floor((0.4*line_length))
    check2 = math.floor((0.7*line_length))
    line_width = len(lines[i][1])
    while j < line_width:
        if (lines[i][check1][j]==0 or lines[i][check2][j]==0) and flag==0:
            temp=[]
            temp.append(i)
            temp.append(j-25)
            word_index.append(temp)
            flag=1
        if lines[i][check1][j]>150 and lines[i][check2][j]>150 and flag==1:
            check+=1
        if check >= 150:
            temp=[]
            temp.append(i)
            temp.append(j)
            word_index.append(temp)
            flag=0
            check=0
        j+=1
    j=0
    
