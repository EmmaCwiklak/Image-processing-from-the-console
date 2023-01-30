import cv2 as cv
import argparse
from functions import rescaleFrame, resizing, gray, blur, canny

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='cat.jpg', help='path to your picture')
    parser.add_argument("--operation", default='display', help='choose edit operation')
    parser.add_argument("--x", help='x', default=5, type=int)
    parser.add_argument("--y", help='y', default=5, type=int)


    args = parser.parse_args()
    print(args.file)
    print(args.operation)
    print(args.x)
    print(args.y)
    x = int(args.x)
    y = int(args.y)
    if args.operation == "display":
        # wyswietlanie obrazu
        img = cv.imread(args.file)
        img = rescaleFrame(img, x)
        cv.imshow(f'{args.file}', img)
    elif args.operation == "resize":
        img = cv.imread(args.file)
        resizing(args.file)
        cv.imwrite('resize.jpg', img) #nie zapisuje
    elif args.operation == "cutsmth": #dziala
        img = cv.imread(args.file)
        img = img[0:x, 0:y, :]
        cv.imshow('Cutted', img)
        cv.imwrite('cut.jpg', img)
    elif args.operation == "gray": #dziala
        img = cv.imread(args.file)
        img = gray(img)
        cv.imwrite('szare.jpg', img)
    elif args.operation == "blur": #dziala
        img = cv.imread(args.file)
        img = blur(img,x)
        cv.imwrite('blur.jpg', img)
    elif args.operation == "canny": #dziala
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
