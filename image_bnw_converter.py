# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:37:40 2019

@author: Deepankar
"""
from PIL import Image
 
def black_and_white_dithering(input_image_path,
    output_image_path,
    dithering=True):
    color_image = Image.open(input_image_path)
    if dithering:
        bw = color_image.convert('1')  
    else:
        bw = color_image.convert('1',
 
    dither=Image.NONE)
    bw.save(output_image_path)
 
if __name__ == '__main__':
    black_and_white_dithering(
        'Test_image.png',
        'Test_image_bnw.png')