import numpy as np
import cv2
import os


# define the color ranges (Using lab 4 to determine Hue values)
colors = [
	[(40, 80, 0), (65, 255, 255), 'Green'], # Green
	[(0, 100, 140), (25, 255, 255), 'Yellow'], # Yellow
	[(80, 5, 5), (126, 255, 255), 'Blue'], # Blue
	[(0, 170, 65), (25, 255, 255), 'Red'] # Red
]

# Play each video in the videos directory
for video in os.listdir('./videos'):

	# Only play video files
	if not video.endswith('.mp4'):
		print("Skipping {}".format(video))
		continue

	# Create a capture stream for the current video
	cap = cv2.VideoCapture('./videos/{}'.format(video))

	while True:

		# grab the current frame and determine if we're still reading data
		playing, frame = cap.read()

		# if we are viewing a video and we did not grab a frame,
		# then we have reached the end of the video
		if not playing:
			break

		# Convert to hsv colorspace for easier hue tracking (As seen in lab 4)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		for color in colors:

			# Mask out the specific color as seen in part b of lab 4
			mask = cv2.inRange(hsv, color[0], color[1])

			# Remove as much noise as possbile
			mask = cv2.erode(mask, None, iterations=4)
			mask = cv2.dilate(mask, None, iterations=4)

			# Find the contours -- Followed this tutorial: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
			# Modified to track multiple objects using contours
			contours = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

			# For each of the contours we need to draw a box around it
			for contour in contours:

				# Use OpenCV to determine the edges of the contour
			    x, y, w, h = cv2.boundingRect(contour)

			    # Draw a rectangle around the object and then state the location and color
			    # This is similar to what was done in lab 5
			    cv2.rectangle(frame, (x-5, y-5), (x+w+5, y+h+5), (0, 255, 0), 2)
			    cv2.putText(frame, color[2] + ' ({}, {})'.format(x, y), (x, y+h), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0 ,0), 2)


		# Show the updated frame with the tracking information
		cv2.imshow(video, frame)

		# if the 'q' key is pressed, stop the loop
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

	# Remove the window and stop the capture once we're done with it
	cap.release()
	cv2.destroyAllWindows()
