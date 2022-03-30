import cv2
import numpy as np

# TODO load images in grey and color
img_gray = cv2.imread('images/logo.png', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('images/logo.png', cv2.IMREAD_COLOR)

# TODO do some print out about the loaded data
print(type(img_gray))
print(type(img_color))

print(img_gray.shape)
print(img_color.shape)

# TODO Continue with the color image or the grayscale image

# TODO Extract the size or resolution of the image

# TODO resize image

new_width = 250
new_height = 250
new_size = (new_width, new_height)
img_color = cv2.resize(img_color, new_size)

# TODO print first row

# TODO print first column

# TODO set an area of the image to black

# TODO find all used colors in the image
all_rgb_codes = img_color.reshape(-1, img_color.shape[-1])
print(all_rgb_codes)
unique_rgb_codes = np.unique(all_rgb_codes, axis=0, return_counts=True)
print(unique_rgb_codes)

# TODO copy one part of an image into another one
# letters = img_color[30:105, 5:130]
# img_color[115:190, 150:275] = letters


# TODO save image

# TODO show the image
# cv2.imshow('tut02', img_color)


# TODO show the original image (copy demo)
title = 'OpenCV Python Tutorial'
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.imshow(title, img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()