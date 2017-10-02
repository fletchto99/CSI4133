#!/usr/local/bin/python3
import numpy as np
import cv2

# Part A
img = cv2.imread('field.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Part A',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('parta.jpg',img)

# # Part B
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
img = cv2.resize(img, (0,0), fx=4, fy=4)
cv2.imshow('Part B',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('partb.jpg',img)

# Part C
img = cv2.imread('field.jpg', cv2.IMREAD_COLOR)
samples = img.reshape((-1,3))

# define criteria, number of clusters(K) and apply kmeans()
ret,label,center = cv2.kmeans(
	np.float32(samples), # Data to quantize
	32, # Quantize to 32 levels
	None,
	(
		cv2.TERM_CRITERIA_MAX_ITER,
		3,
		1
	),
	3,
	cv2.KMEANS_RANDOM_CENTERS
)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
img = res.reshape((img.shape))

cv2.imshow('Part C',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('partc.jpg',img)
