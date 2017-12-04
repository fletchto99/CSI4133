# Matthew Langlois
# Student # 7731813

#!/usr/local/bin/python3
import cv2
import numpy as np

img = cv2.imread('images/circles_target.jpg', cv2.IMREAD_COLOR)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, 1.02, 75)

if not circles.any():
	print("No circles found!")
	cv2.imshow('Circles',grayscale)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else:
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
	    # draw the outer circle
	    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	    # draw the center of the circle
	    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

	cv2.imshow('Circles',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
