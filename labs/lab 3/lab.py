#!/usr/local/bin/python3

# Matthew Langlois
# Student # 7731813
import cv2
import numpy as np


cap = cv2.VideoCapture('./video/park.avi')
out = cv2.VideoWriter('./results/park.avi', -1, 1, (320,240))

# Get the first frame, needed to compute difference
last_gray = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)

while(cap.isOpened()):
    ret, frame = cap.read()

    # Exit when done reading the video
    if not ret:
    	break

    # Convert to greyscale
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Compute the difference between the frames
    img = np.absolute(frame - last_gray)

    # Only look at a specific threshold
    ignore, processed = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

    last_gray = frame
    out.write(processed)
    cv2.imshow('Video',processed)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()
