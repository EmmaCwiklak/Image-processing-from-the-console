import cv2 as cv
import argparse
from functions import rescaleFrame,resizing, obrot,gray, blur, canny
from UserOutputs import pathInput, selectingEdiction

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='logo.jpg', help='path to your picture')
    parser.add_argument("--operation", default='display', help='choose edit operation')
    parser.add_argument("--x", help='x', default=500, type=int)
    parser.add_argument("--y", help='y', default=500, type=int)


    args = parser.parse_args()
    print(args.file)
    print(args.operation)
    print(args.x)
    print(args.y)

    if args.operation == "display":
        # wyswietlanie obrazu
        img = cv.imread(args.file)
        resized_image = rescaleFrame(img)
        cv.imshow(f'{args.file}', resized_image)
    elif args.operation == "resize":
        img = cv.imread(args.file)
        resizing(args.file)
        cv.imwrite('resize.jpg', img)
    elif args.operation == "cutsmth":
        img = cv.imread(args.file)
        x = args.x
        y = args.y
        img = img[0:x, 0:y, :]
        cv.imshow('Cutted', img)
        cv.imwrite('cut.jpg', img)
    elif args.operation == "obrot":
        img = cv.imread(args.file)
        img = obrot(img)
        cv.imwrite('obrocone.jpg', img)
    elif args.operation == "gray":
        img = cv.imread(args.file)
        img = gray(img)
        cv.imwrite('szare.jpg', img)
    elif args.operation == "blur":
        img = cv.imread(args.file)
        img = blur(img)
        cv.imwrite('blur.jpg', img)
    elif args.operation == "canny":
        img = cv.imread(args.file)
        img = canny(img)
        cv.imwrite('canny.jpg', img)
    elif args.operation == "canny":
        img = cv.imread(args.file)
        img = canny(img)
        cv.imwrite('canny.jpg', img)



    cv.waitKey(0)

if __name__ == '__main__':
    main()
