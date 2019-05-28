# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:59:14 2019

@author: Deepankar
"""

import cv2

image = cv2.imread('Test_image_bnw1.png')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAYSCALE)


height = len(img)

flag=0
start = []
stop = []

final_img = []


for i in range(height):
    if img[i][10]==255 and flag==0:
        start.append(i)
        flag=1
        continue
    if img[i][10]==255 and flag==1:
        stop.append(i)
        flag=0
        continue
        

for i in range(len(stop)):
    print(start[i])
    print(stop[i])
    print()
'''
  r1 = stop[1]-start[1]
  
for i in range(r1):
    for j in range(2843):
        final_img.append(r1,j)
print(final_img)'''