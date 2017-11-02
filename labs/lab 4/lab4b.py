# Matthew Langlois
# Student # 7731813

#!/usr/local/bin/python3
import numpy as np
import cv2

img = cv2.imread('images/Picture3.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Part B - dds', hsv)

yellowgreen = [np.array([34,100, 100]), np.array([37,255,255])]
violet = [np.array([128,70, 70]), np.array([131,255,255])]
red = [np.array([0,150, 150]), np.array([0,255,255])]

# We don't need to do anything on change
def change(value):
    #read the image as grayscale
    arr = yellowgreen;
    if value == 1:
        arr = violet
    elif value == 2:
        arr = red

    threshold = cv2.inRange(hsv, arr[0], arr[1])

    res = cv2.bitwise_and(img,img, mask=threshold)

    # Show and return the image
    cv2.imshow('Part B - mask', threshold)
    cv2.imshow('Part B - result', res)
    print(value)

cv2.namedWindow('Part B - mask')
cv2.namedWindow('Part B - result')
cv2.createTrackbar('Threshold', 'Part B - result', 0, 2, change);
change(0)

# Press any key to refresh the windows
cv2.waitKey(0)

