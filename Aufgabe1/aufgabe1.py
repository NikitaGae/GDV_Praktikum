import cv2
import numpy as np
import math
import operator

#creates an empty image
img = np.zeros((900, 900), dtype=np.uint8)
#fills it with a colour gradient
for i in range(900):
    img[:, i] = i/4

#copies a square out of the middle of the img
copiedSquare = img[400:500, 400:500]

#switches a area on the img with the copied square
img[120:220, 120:220] = copiedSquare
img[680:780, 680:780] = copiedSquare

#function to create the path of a circle
def circle_path(t, scale, offsetx, offsety):
    res = (int(scale*math.cos(t)+offsety), int(scale*math.sin(t)+offsetx))
    return res


timer = 0.0

while True: 

#create a copy of our image
    img2 = img.copy()
    #draws the square in a circular path
    timer += 0.005
    pt1 = circle_path(timer, 400, 400, 400)
    size = (100, 100)
    pt2 = tuple(map(operator.add, pt1, size))
    img2[pt1[1]:pt2[1], pt1[0]:pt2[0]] = copiedSquare

    # display the image
    cv2.imshow("ILLUSION", img2)

    # press q to close the window
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()