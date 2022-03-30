import numpy as np
import cv2

# print keyboard usage
print('This is a HSV color detection demo. Use the keys to adjust the \
selection color in HSV space. Circle in bottom left.')
print('The masked image shows only the pixels with the given HSV color within \
a given range.')
print('Use h/H to de-/increase the hue.')
print('Use s/S to de-/increase the saturation.')
print('Use v/V to de-/increase the (brightness) value.\n')

# capture webcam image
cap = cv2.VideoCapture(0)

# get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))
print('Video properties:')
print('  Width = ' + str(width))
print('  Height = ' + str(height))
print('  Codec = ' + str(codec))

# drawing helper variables
thick = 10
thin = 3
thinner = 2
font_size_large = 3
font_size_small = 1
font_size_smaller = .6
font = cv2.FONT_HERSHEY_SIMPLEX


def color_picker(event, x, y, flags, param):
    global hue, saturation, value
    if event == cv2.EVENT_LBUTTONDBLCLK:
        (h, s, v) = hsv[y, x]
        hue = int(h)
        saturation = int(s)
        value = int(v)
        print('New color selected:', (hue, saturation, value))


# TODO define  RGB colors as variables
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# exemplary color conversion (only for the class), tests usage of cv2.cvtColor

# color ranges, TODO enter found default values and uncomment
hue = 120
hue_range = 10
saturation = 200
saturation_range = 100
value = 90
value_range = 100

while True:
    # get video frame (always BGR format!)
    ret, frame = cap.read()
    if (ret):
        # copy image to draw on
        img = frame.copy()

        # TODO draw arrows (coordinate system)
        img = cv2.arrowedLine(img, (10, 10), (100, 10), blue, thin)
        img = cv2.putText(img, 'X', (115, 25), font,
                          font_size_small, blue, thin)

        # TODO computing color ranges for display
        lower_blue = np.array([hue - hue_range,
                               saturation - saturation_range,
                               value - value_range])
        upper_blue = np.array([hue + hue_range,
                               saturation + saturation_range,
                               value + value_range])
        HSV_blue_img = np.zeros((1, 1, 3), np.uint8)
        HSV_blue_img[0, 0] = (hue, saturation, value)
        medium_blue_array = cv2.cvtColor(HSV_blue_img, cv2.COLOR_HSV2BGR)[0, 0]
        blue_BGR = (int(medium_blue_array[0]), int(
            medium_blue_array[1]), int(medium_blue_array[2]))

        # TODO draw selection color circle and text for HSV values
        
        # convert to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # create a mask
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # apply mask
        result = cv2.bitwise_and(img, img, mask=mask)

        # TODO show the original image with drawings in one window
        title = 'original'
        cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
        cv2.setMouseCallback(title, color_picker)
        cv2.imshow(title, img)
        # TODO show the masked image in another window
        
        # TODO show the mask image in another window

        # TODO deal with keyboard input

    if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Could not start video camera')
        break

cap.release()
cv2.destroyAllWindows()
