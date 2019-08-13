import numpy as np
import cv2

img = cv2.imread('data/img.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
binary = cv2.bitwise_not(gray)

# cv2.imshow('temp',binary)
# cv2.waitKey(0)

(_,contours,_) = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
ori = cv2.imread('data/put.png')

for contour in contours:
    (x,y,w,h)=cv2.boundingRect(contour)
    dim=(w,h)
    ori=cv2.resize(ori,dim)
    # cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    img[y:y+h,x:x+w]=ori

cv2.imshow('temp',img)
cv2.waitKey(0)