# Matthew Langlois
# Student # 7731813

#!/usr/local/bin/python3
import numpy as np
import cv2

img = cv2.imread('./images/hand.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# We don't need to do anything on change
def change(value):
    #read the image as grayscale


    threshold = cv2.inRange(hsv, np.array([value,180,0]), np.array([value+10,255,255]))

    res = cv2.bitwise_and(img,img, mask=threshold)

    # Show and return the image
    cv2.imshow('Part A', res)
    print(value)


cv2.namedWindow('Part A - HSV')
cv2.imshow('Part A - HSV', hsv)
cv2.namedWindow('Part A')
cv2.imshow('Part A', img)
cv2.createTrackbar('Threshold', 'Part A', 0, 180, change);

# Press any key to refresh the windows
cv2.waitKey(0)

