import numpy as np
import cv2

# TODO capture webcam image
cap = cv2.VideoCapture(0)

# TODO get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# TODO create a window for the video
title = 'Video'
cv2.namedWindow(title, cv2.WINDOW_FREERATIO)

# TODO start a loop
while True:

    # TODO (in loop) read a camera frame and check if that was successful
    ret, frame = cap.read()
    if (ret):
        pass
        # TODO (in loop) create four flipped tiles of the image

        # TODO (in loop) display the image
        cv2.imshow(title, frame)
    else:
        pass
    # TODO (in loop) press q to close the window and exit the loop
    if cv2.waitKey(10) == ord('q'):
        break
# TODO release the video capture object and window
