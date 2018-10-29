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
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cnt = []    
for contour in contours:
    
    ep  = 0.001*cv2.arcLength(contour, True)
    approxShape = cv2.approxPolyDP(contour, ep, False)
    cnt.append(approxShape)


cv2.drawContours(img, cnt, -1, (0,255,0), 3)
cv2.imshow("Ear", img)
cv2.waitKey()

quit()

# print 'Contours found: {}\n'.format(len(contours))
# print 'Press any key...\n'

# while True:

#     cv2.imshow('Ear', img)

#     ch = cv2.waitKey()

#     if ch != None:
#         cv2.destroyAllWindows()
#         x = int(input("Contour to display: "))
#         # Draw contours
#         img = cv2.drawContours(img, contours[x], -1, (0,255,0), 3)
#         ch = None
        
