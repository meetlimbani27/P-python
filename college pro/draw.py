import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3) , dtype='uint8')            # creates a blank image to draw on , uint8 means image
cv.imshow('Blank', blank) 


# # 1. Paint image a certain color
# blank[200:300, 300:400] = 0,255,0         # [:] refrences all pixels ,BGR  ,  color is green
# cv.imshow('Green', blank)


# # 2. draw rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)          # thickness=cv.FILLED fills whole rectangle or thickness=-1
# cv.imshow('Rectangle', blank)                                           # try   cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2 )


# 3. draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)


# 4. draw line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)
# img = cv.imread('archive/train/apple/Image_1.jpg') 
# cv.imshow('Image', img)

cv.waitKey(0)