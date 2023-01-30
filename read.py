import cv2 as cv
import argparse
from functions import rescaleFrame, resizing, gray, blur, canny

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='cat.jpg', help='path to your picture')
    parser.add_argument("--operation", default='display', help='choose edit operation')
    parser.add_argument("--x", "-x", help='x', default=5, type=int)
    parser.add_argument("--y", "-y", help='y', default=5, type=int)
    parser.add_argument("--r", "-r", help='red', default=255, type=int)
    parser.add_argument("--g", "-g", help='green', default=255, type=int)
    parser.add_argument("--b", "-b", help='blue', default=255, type=int)
    args = parser.parse_args()
    print(args.file)
    print(args.operation)
    print(args.x)
    print(args.y)
    x = int(args.x)
    y = int(args.y)
    b = int(args.b)
    g = int(args.g)
    r = int(args.r)

    img = cv.imread(args.file)

    def cutsmth():
        img = cv.imread(args.file)
        img = img[0:x, 0:y, :]
        cv.imshow('Cutted', img)
        cv.imwrite('cut.jpg', img)

    def resize():
        img = cv.imread(args.file)
        img = resizing(img, x)
        cv.imwrite('resize.jpg', img)
    def display(img,x):
        if x != 5:
            img = rescaleFrame(img, x)
            cv.imshow(f'{args.file}', img)
        else:
            img = rescaleFrame(img, 0.5)
            cv.imshow(f'{args.file}', img)
        cv.waitKey(0)

    def cos():
        print("cos")

    switcher = {
        "cutsmth": cutsmth(),
        "resize": resize(),
        "display": display(img, x),
        "cos": cos()
    }

    def switch(args):
        return switcher.get(args.operation)()
"""
 if args.operation == "display":
        # wyswietlanie obrazu
        if args.x != 5:
            img = rescaleFrame(img, x)
            cv.imshow(f'{args.file}', img)
        else:
            img = rescaleFrame(img, 0.5)
            cv.imshow(f'{args.file}', img)
    elif args.operation == "resize": #dziala
        img = resizing(img,x)
        cv.imwrite('resize.jpg', img)
    elif args.operation == "cutsmth": #dziala
        img = img[0:x, 0:y, :]
        cv.imshow('Cutted', img)
        cv.imwrite('cut.jpg', img)
    elif args.operation == "gray": #dziala
        img = gray(img)
        cv.imwrite('szare.jpg', img)
    elif args.operation == "blur": #dziala
        img = blur(img,x)
        cv.imwrite('blur.jpg', img)
    elif args.operation == "canny": #dziala
        img = canny(img)
        cv.imwrite('canny.jpg', img)
    elif args.operation == "split":

        merged = cv.merge([b,g,r])
        cv.imshow("Merged Image", merged)

    cv.waitKey(0)
"""


if __name__ == '__main__':
    main()

