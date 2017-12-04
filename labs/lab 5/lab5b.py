# Matthew Langlois
# Student # 7731813

#!/usr/local/bin/python3
import cv2
import numpy as np

img = cv2.imread('images/lines_target.jpg', cv2.IMREAD_COLOR)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grayscale, 50, 150)
lines = cv2.HoughLines(edges, 1, np.pi/180, 130)

if not lines.any():
	print("No lines found!")
	cv2.imshow('Lines',grayscale)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else:
	for line in lines:
		for rho,theta in line:
		    print("test")
		    a = np.cos(theta)
		    b = np.sin(theta)
		    x0 = a*rho
		    y0 = b*rho
		    x1 = int(x0 + 1000*(-b))
		    y1 = int(y0 + 1000*(a))
		    x2 = int(x0 - 1000*(-b))
		    y2 = int(y0 - 1000*(a))

		    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

	#TODO: Print intersections

	cv2.imshow('Lines',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
