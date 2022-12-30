import cv2 as cv
from functions import rescaleFrame
from UserOutputs import pathInput, selectingEdiction

path=pathInput()
img = cv.imread(path)

resized_image = rescaleFrame(img)
cv.imshow(f'{path}',resized_image)

selectingEdiction()
#cv.waitKey(0) #czeka na jakis
