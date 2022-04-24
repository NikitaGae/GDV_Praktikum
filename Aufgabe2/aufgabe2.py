import cv2
from cv2 import erode
import numpy as np
import glob

# Goal: Count the number of blue chewing gums in the images
# define blue in HSV
hue = 100  
hue_range = 10
saturation = 155
saturation_range = 100
value = 250
value_range = 100
lower_blue = np.array([hue - hue_range, saturation -
                       saturation_range, value - value_range])
upper_blue = np.array([hue + hue_range, saturation +
                       saturation_range, value + value_range])

# define different shapes for kernel
def morph_shape(val):
    if val == 0:
         return cv2.MORPH_RECT
    elif val == 1:
         return cv2.MORPH_CROSS
    elif val == 2:
         return cv2.MORPH_ELLIPSE


# dilation with parameters
def dilatation(img, size, shape):
    kernel = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                    (size, size))
    return cv2.dilate(img, kernel)


# erosion with parameters
def erosion(img, size, shape):
    kernel = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                        (size, size))
    return cv2.erode(img, kernel)

# opening with parameters
def opening(img, size, shape):
    kernel = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                        (size, size))
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# closing with parameters
def closing(img, size, shape):
    kernel = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                        (size, size))
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


for img_name in glob.glob("gdv-SoSe2022/images/chewing_gum_balls*.jpg"):
    print('Searching for colored balls in image:', img_name)

    #reading image
    img = cv2.imread( img_name, cv2.IMREAD_COLOR)
    # convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   
    # create a mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # apply morphological operations
    kernel_size = 3
    kernel_shape = morph_shape(2)
    mask = opening(mask, kernel_size, kernel_shape)
    mask = erosion(mask, kernel_size, kernel_shape)
    mask = closing(mask, kernel_size, kernel_shape)

    # find connected components
    connectivity = 8
    (numLabels, labels, stats, centroids) = cv2.connectedComponentsWithStats(
        mask, connectivity, cv2.CV_32S)

    # helper variables for drawing and candidate rejection
    red_BGR = (0, 0, 255)
    green_BGR = (0, 255, 0)
    circle_size = 10
    circle_thickness = 5
    min_size = 11
    expected_roundness = 0.1
    numRejected = 1

    # go through all (reasonable) found connected components
    for i in range(1, numLabels):
        # check size and roundness as plausibility
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        if w < min_size or h < min_size:
            print('Found a too small component.')
            numRejected += 1
            continue  # found component is too small to be correct
        if w >= h:
            roundness = 1.0 / (w/h)
        elif h > w:
            roundness = 1.0 / (h/w)
        if (roundness < expected_roundness):
            print('Found a component that is not round enough.')
            numRejected += 1
            continue  # ratio of width and height is not suitable
    

        # find and draw center
        center = centroids[i]
        center = np.round(center)
        center = center.astype(int)
        cv2.circle(img, center, circle_size, red_BGR, circle_thickness)

        cv2.rectangle(img, (x, y), (x + w, y + h), green_BGR, 3)

    # print out number of connected components
    print('We have found', str(numLabels-numRejected), 'blue chewing gums.')

    # show the original image with drawings in one window
    cv2.imshow(img_name, img)
    # show the masked image in another window

    # show the mask image in another window
    cv2.imshow("Mask image", mask)
    cv2.imwrite("mask.jpg", mask)

    key = cv2.waitKey(0)
    if key == ord('q'):
        break

    cv2.destroyAllWindows()