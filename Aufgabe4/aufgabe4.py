from GDV_TrainingSet import Descriptor, TrainingSet
import cv2
import numpy as np

# splits the image in sections, finds the best match for them and saves them to a new image
def getRois(img, nRows, mCols):
    width = img.shape[1]
    height = img.shape[0]

    img_mosaic = np.zeros(img.shape, np.uint8)

    for i in range(0, nRows):
        for j in range(0, mCols):
            roi = img[int(i * (height/nRows)):int((i * height/nRows + height/nRows)), int(j * width / mCols):int(j * width / mCols + width / mCols)]
            print(roi.shape)
            assert(isinstance(trainData.descriptor, Descriptor))
            descr = trainData.descriptor
            newcomer = np.ndarray(shape=(1, descr.getSize()),
                                  buffer=np.float32(descr.compute(roi)),
                                  dtype=np.float32)
            idx = findBestMatch(trainData, newcomer)
            best_matching_img = cv2.imread(trainData.getFilenameFromIndex(idx), cv2.IMREAD_COLOR)
            best_matching_img = cv2.resize(best_matching_img, (roi.shape[1], roi.shape[0]))

            img_mosaic[int(i * (height/nRows)):int((i * height/nRows + height/nRows)), int(j * width / mCols):int(j * width / mCols + width / mCols)] = best_matching_img
            
    cv2.imshow("title", img_mosaic)
    # filename = 'savedImageNIKE.jpg'
    filename = 'savedImageKATZE.jpg'
    # Saving the image
    cv2.imwrite(filename, img_mosaic)
    cv2.waitKey(0)
    return img_mosaic


n = 60
m = 60  


def findBestMatch(trainData, sample):
    # do the matching with FLANN
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(trainData.trainData, sample, k=1)
    # Sort by their distance.
    matches = sorted(matches, key =lambda x: x[0].distance)
    bestMatch = matches[0][0]
    return bestMatch.queryIdx


# Define and compute or load the training data
root_path = 'Aufgabe4/data/101_ObjectCategories/'
file_name = 'Aufgabe4/data/data.npz'
trainData = TrainingSet(root_path)
# either create and save the data
trainData.createTrainingData(Descriptor.TINY_GRAY4)
trainData.saveTrainingData(file_name)
# or load the saved data if descriptor has not been changed.
# trainData.loadTrainingData(file_name)

# read image you want to make a mosaic of
# newImg = cv2.imread('Aufgabe4/data/nike.jpg', cv2.IMREAD_COLOR)
newImg = cv2.imread('Aufgabe4/data/katze.jpg', cv2.IMREAD_COLOR)
cv2.imshow('query image', newImg)

getRois(newImg, n, m)