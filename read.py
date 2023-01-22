import cv2 as cv
import argparse
from functions import rescaleFrame,resizing
from UserOutputs import pathInput, selectingEdiction

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='logo.jpg', help='path to your picture')
    parser.add_argument("--operation", default='display', help='choose edit operation')
    parser.add_argument("--x",action='append', help="size of cutted area")
    parser.parse_args("--x x ".split())


    args = parser.parse_args()
    print(args.file)
    print(args.operation)

    if args.operation == "display":
        # wyswietlanie obrazu
        img = cv.imread(args.file)
        cv.imshow(f'{args.file}', img)
    elif args.operation == "resize":
        img = cv.imread(args.file)
        resizing(args.file)
        cv.imwrite('save.jpg', img)
    elif args.operation == "cutsmth":
        img = cv.imread(args.file)
        x=args.file.x[0]
        img = img[x:x, x:x, :]
        cv.imwrite('save2.jpg', img)



    cv.waitKey(0)

if __name__ == '__main__':
    main()

"""
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
"""