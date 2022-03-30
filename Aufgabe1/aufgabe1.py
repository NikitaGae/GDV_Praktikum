import cv2
import numpy as np
import math
import operator

img = np.zeros((900, 900), dtype=np.uint8)
for i in range(900):
    img[:, i] = i/4

copiedSquare = img[400:500, 400:500]
img[50:150, 50:150] = copiedSquare
img[650:750, 750:850] = copiedSquare


def circle_path(t, scale, offset):
    res = (int(scale*math.cos(t)+offset), int(scale*math.sin(t)+offset))
    return res


timer = 0.0
red = (255, 0, 0)
thin = 3


while True:
    # draw a rectangle that moves on a circular path
    timer += 0.2
    pt1 = circle_path(timer, 350, 300)
    size = (20, 20)
    pt2 = tuple(map(operator.add, pt1, size))
    img = cv2.rectangle(img, pt1, pt2, red, thin)

    # display the image
    cv2.imshow('Video image', img)

    # press q to close the window
    if cv2.waitKey(10) == ord('q'):
        break


# release the video capture object and window
img.release()
cv2.destroyAllWindows()