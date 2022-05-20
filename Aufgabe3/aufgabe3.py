import numpy as np
import cv2

ref_pt_src = []
ref_pt_dst = []
kernelsize = 15
sigma = 7
sigmaLaplace = 3

def click_src(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt_src
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(ref_pt_src)
        if (pos == 0):
            ref_pt_src = [(x, y)]
        else:
            ref_pt_src.append((x, y))
        # draw a circle at the clicked position
        cv2.circle(img, ref_pt_src[pos], 4, (0, 255, 0), 2)
        cv2.imshow('Original', img)


def click_dst(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt_dst
    # if the left mouse button was clicked,
    # add the point to the destination array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(ref_pt_dst)
        if (pos == 0):
            ref_pt_dst = [(x, y)]
        else:
            ref_pt_dst.append((x, y))
        # draw a circle at the clicked position
        cv2.circle(dst_transform, ref_pt_dst[pos], 4, (0, 255, 0), 2)
        cv2.imshow('Transformed image', dst_transform)

#define a highpass filter function
def highpass(img,kernelsize, sigma):
    return img - cv2.GaussianBlur(img,(kernelsize,kernelsize) , sigma) + 127
#or choose the laplace instead of the highpass
def laplace(img,sigma,kernelsize):
    return   cv2.Laplacian(img,-1,sigma,kernelsize)+127
#define a lowpass filter function
def lowpass(img,sigma,kernelsize):
    return cv2.GaussianBlur(img,(kernelsize,kernelsize),sigma)

#read and resize first image
img = cv2.imread("Images/Aufgabe3/hund.png", cv2.IMREAD_COLOR)
img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
#apply lowpass to first img and show it after
img = lowpass(img, kernelsize,sigma)
cv2.imshow('bild lowpass', img)

#read and resize second image
img2 = cv2.imread("Images/Aufgabe3/katze.png", cv2.IMREAD_COLOR)
img2 = cv2.resize(img2, (500, 500), interpolation=cv2.INTER_CUBIC)
#apply lowpass to second img and show it after
img2 = highpass(img2,kernelsize,sigmaLaplace)
cv2.imshow('bild laplace', img2)


rows, cols, dim = img.shape
clone = img.copy()
clone2 = img2.copy()
dst_transform = img2
cv2.namedWindow('Original')
cv2.setMouseCallback('Original', click_src)
cv2.namedWindow('Transformed image')
cv2.setMouseCallback('Transformed image', click_dst)

computationDone = False
while True:
    # makes the code only use the last 3 clicks
    if(len(ref_pt_src) > 3):
        ref_pt_src.pop(0)
        computationDone = False

    if(len(ref_pt_dst) > 3):
        ref_pt_dst.pop(0)
        computationDone = False
    # if there are three reference points, then compute the transform and apply the transformation
    if not(computationDone) and (len(ref_pt_src) == 3 and len(ref_pt_dst) == 3):
        T_affine = cv2.getAffineTransform(np.float32(ref_pt_src), np.float32(ref_pt_dst))
        print('\nAffine transformation:\n', '\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_affine]))
        dst_transform = cv2.warpAffine(img, T_affine, (cols, rows))
        
        dst_transform = cv2.add(img2//2,dst_transform//2)
        computationDone = True

    # display the image and wait for a keypress
    cv2.imshow('Original', img)
    cv2.imshow('Transformed image', dst_transform)
    key = cv2.waitKey(10)

    # if the 'r' key is pressed, reset the transformation
    if key == ord("r"):
        dst_transform=clone2.copy()
        img = clone.copy()
        ref_pt_src = []
        ref_pt_dst = []
        computationDone = False
    # if the 'q' key is pressed, break from the loop
    elif key == ord("q"):
        break

cv2.destroyAllWindows()
