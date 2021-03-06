# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EADZCvVUeMYbkgcZgSyvqlREE9hKCTn6
"""

import cv2
import numpy as np

def getTextOverlay(input_image):
    kernel = np.ones((5,5), np.uint8)
    image_dilated = cv2.dilate(input_image, kernel)
    ret, thresh = cv2.threshold(image_dilated, 50, 255, cv2.THRESH_BINARY_INV)
    output = cv2.bitwise_not(thresh)
    # Write your code here for output
    
    return output

if __name__ == '__main__':
    image = cv2.imread('/content/simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)