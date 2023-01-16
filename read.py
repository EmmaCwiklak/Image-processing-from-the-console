import cv2 as cv
import argparse
from functions import rescaleFrame
from UserOutputs import pathInput, selectingEdiction

def main():
    file = argparse.ArgumentParser()

    file.add_argument('-f', '--file', action='store', dest='path_from', default='cat.jpg',help='path to your file')
    results = file.parse_args()

    rescale = argparse.ArgumentParser()
    rescale.add_argument('-rs','--rescale', dest='accumulate', action='store',help='rescale displayed image')
    display = rescale.parse_args()

    img = cv.imread(results.path_from)

    resized_image = rescaleFrame(img)
    cv.imshow(f'{results}', resized_image)

#selectingEdiction()

    cv.waitKey(0) #czeka na jakis

if __name__ == '__main__':
    main()

