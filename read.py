import cv2 as cv
import argparse
from functions import rescaleFrame
from UserOutputs import pathInput, selectingEdiction

def main():
#path=pathInput()
    file = argparse.ArgumentParser()
    file.add_argument('-f', '--file', action='store', dest='path_from', default='cat.jpg',help='path to your file')
    results= file.parse_args()

    img = cv.imread(results.path_from)

    resized_image = rescaleFrame(img)
    cv.imshow(f'{results}', resized_image)

#selectingEdiction()
    cv.waitKey(0) #czeka na jakis

if __name__ == '__main__':
    main()

"""import cv2, argparse
from functions import rescaleFrame
from UserOutputs import pathInput, selectingEdiction

def main():
    file = argparse.ArgumentParser(description='input path to photo')

    file.add_argument('-f', '--file', action='store', dest='path_from', default='cat.jpg', help='path to your file')
    results = file.parse_args()

    img = cv2.imread(results.path_from)
    cv2.waitKey(0) #zamknie okno jak cos nacisne


    #ustalanie wielkosci okna
    #resized_image = rescaleFrame(img)
    #cv2.imshow(f'{results.path_from}', resized_image)


    #selectingEdiction()

if __name__ == '__main__':
    main()
"""