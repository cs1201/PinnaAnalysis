import numpy
import cv2
import os
import argparse

img = cv2.imread('ear.jpg')

cv2.namedWindow('Ear')
cv2.imshow('Ear', img)

#Find contours 
imRay = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imRay,190, 255,cv2.THRESH_BINARY)


cv2.imshow("Ear", thresh)
cv2.waitKey()

quit()