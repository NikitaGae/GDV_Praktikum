from GDV_TrainingSet import Descriptor, TrainingSet
import cv2
import numpy as np


def getRois(img, nRows, mCols):
    width = img.shape[1]
    height = img.shape[0]

    img_mosaic = np.zeros(img.shape, np.uint8)

    for i in range(0, nRows):
        for j in range(0, mCols):
            roi = img[int(i * (height/nRows)):int((i * height/nRows + height/nRows)), int(j * width / mCols):int(j * width / mCols + width / mCols)]
            # cv2.imshow("title", roi)
            # cv2.waitKey(0)
            print(roi.shape)
            assert(isinstance(trainData.descriptor, Descriptor))
            descr = trainData.descriptor
            newcomer = np.ndarray(shape=(1, descr.getSize()),
                                  buffer=np.float32(descr.compute(roi)),
                                  dtype=np.float32)
            idx = findBestMatch(trainData, newcomer)
            best_matching_img = cv2.imread(trainData.getFilenameFromIndex(idx), cv2.IMREAD_COLOR)
            best_matching_img = cv2.resize(best_matching_img, (roi.shape[1], roi.shape[0]))

           # cv2.imshow('best match', best_matching_img)
            img_mosaic[int(i * (height/nRows)):int((i * height/nRows + height/nRows)), int(j * width / mCols):int(j * width / mCols + width / mCols)] = best_matching_img
            
    cv2.imshow("title", img_mosaic)
    cv2.waitKey(0)
    return img_mosaic


n = 60
m = 60  


def findBestMatch(trainData, sample):
    # do the matching with FLANN
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(trainData.trainData, sample, k=1)
    # Sort by their distance.
    matches = sorted(matches, key=lambda x: x[0].distance)
    bestMatch = matches[0][0]
    return bestMatch.queryIdx


''' Define and compute or load the training data '''
root_path = 'assignments/a04_image_retrieval/data/101_ObjectCategories/'
# adjust this path if you have the files in some other folder
# root_path = './data/temp/'  # you can use a smaller subset
# of the training data during development to save time
file_name = 'assignments/a04_image_retrieval/data/data.npz'
trainData = TrainingSet(root_path)
# either create and save the data
# trainData.createTrainingData(Descriptor.TINY_GRAY4)
# trainData.saveTrainingData(file_name)
# or load the saved data if descriptor has not been changed.
trainData.loadTrainingData(file_name)

# exemplary test image to check the implementation. As it is part of the
# data set, the best match in the data set needs to be the same image.
newImg = cv2.imread('assignments/a04_image_retrieval/data/nike.jpg', cv2.IMREAD_COLOR)
# newImg = cv2.imread('assignments/a04_image_retrieval/data/101_ObjectCategories/airplanes/image_0005.jpg', cv2.IMREAD_COLOR)
# alternatively use another image and find the best match
# newImg = cv2.imread('images/butterfly.jpg', cv2.IMREAD_COLOR)
cv2.imshow('query image', newImg)


# assure that the same descriptor is used by reading it
# from the training data set


getRois(newImg, n, m)