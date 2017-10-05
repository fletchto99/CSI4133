# Matthew Langlois
# Student # 7731813

#!/usr/local/bin/python3
import numpy as np
import cv2

# Simply display a window with an image
def makeWindow(name, image, x, y):
	cv2.namedWindow(name)
	img = cv2.imread(image, cv2.IMREAD_COLOR)
	cv2.imshow(name, img)
	cv2.moveWindow(name, x, y)

# We don't need to do anything on change
def change(value):
	pass

# Creats a window with a threshold slider
def makeThresholdWindow(name, image, x, y):
	cv2.namedWindow(name)
	#read the image as grayscale
	img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
	cv2.createTrackbar("Threshold", name, 0, 255, change);

	# Add a threshold bar
	threshold = cv2.getTrackbarPos("Threshold", name)

	# Apply the threshold
	ignore, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV);

	# Show and return the image
	cv2.imshow(name, img)
	cv2.moveWindow(name, x, y)
	return img

# Part A

# Show the various frames

makeWindow('Frame 1 - Source 1', 'images/Img02_0076.bmp', 0, 0)
makeWindow('Frame 2 - Source 1', 'images/Img02_0077.bmp', 400, 0)
makeWindow('Frame 3 - Source 1', 'images/Img02_0078.bmp', 800, 0)
makeWindow('Frame 1 - Source 2', 'images/park466.bmp', 0, 300)
makeWindow('Frame 2 - Source 2', 'images/park467.bmp', 400, 300)
makeWindow('Frame 3 - Source 2', 'images/park468.bmp', 800, 300)

# Move to part b when any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# Part B
while(1):
	# Make the threshold windows
	img1 = makeThresholdWindow('Frame 1 - Source 1', 'images/Img02_0076.bmp', 0, 0)
	img2 = makeThresholdWindow('Frame 2 - Source 1', 'images/Img02_0077.bmp', 400, 0)
	img3 = makeThresholdWindow('Frame 3 - Source 1', 'images/Img02_0078.bmp', 800, 0)
	img4 = makeThresholdWindow('Frame 1 - Source 2', 'images/park466.bmp', 0, 300)
	img5 = makeThresholdWindow('Frame 2 - Source 2', 'images/park467.bmp', 400, 300)
	img6 = makeThresholdWindow('Frame 3 - Source 2', 'images/park468.bmp', 800, 300)

	# Press any key to refresh the windows
	k = cv2.waitKey(1)

	# Press escape to quit
	if k == 27:
		cv2.imwrite('results/Img02_0076.bmp',img1)
		cv2.imwrite('results/Img02_0077.bmp',img2)
		cv2.imwrite('results/Img02_0078.bmp',img3)
		cv2.imwrite('results/park466.bmp',img4)
		cv2.imwrite('results/park467.bmp',img5)
		cv2.imwrite('results/park468.bmp',img6)
		cv2.destroyAllWindows()
		break

