import cv2 as cv
import numpy as np
import argparse
from functions import rescaleFrame, resizing, gray, blur, canny, translate, rotate

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='wsb.jpg', help='path to your picture')
    parser.add_argument("--operation", default='default', help='choose edit operation')
    parser.add_argument("--x", "-x", help='x parameter', default=0, type=int)
    parser.add_argument("--y", "-y", help='y parameter', default=0, type=int)
    parser.add_argument("--r", "-r", help='red', default=255, type=float)
    parser.add_argument("--g", "-g", help='green', default=255, type=float)
    parser.add_argument("--b", "-b", help='blue', default=255, type=float)
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

    if args.operation == "default":
        rescaleFrame(img, 0.5)
    elif args.operation == "resize": #dziala
        resizing(img,x)

    elif args.operation == "cutsmth": #dziala
        img = img[0:x, 0:y, :]
        cv.imshow('Cutted', img)
        cv.imwrite('cut.jpg', img)

    elif args.operation == "gray": #dziala
        gray(img)

    elif args.operation == "blur": #dziala
        if x%2==0:
            x+=1
        blur(img,x)

    elif args.operation == "canny": #dziala
        canny(img)

    elif args.operation == "translate": #dziala
        if x==0 and y == 0:
            x=y=100
        translated=translate(img,x,y)
        cv.imshow("Translate",translated)

    elif args.operation == "rotate":
        rotated = rotate(img,x)
        cv.imshow("rotated", rotated)
        cv.imwrite('rotated.jpg', rotated)

    elif args.operation == "flip":
        flip = cv.flip(img, x)
        cv.imshow("flip", flip)
        cv.imwrite('fliped.jpg', flip)

    elif args.operation == "hsv":
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        cv.imshow("HSV", hsv)
        cv.imwrite('hsv.jpg', hsv)
    elif args.operation == "lab":
        lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
        cv.imshow("LAB", lab)
        cv.imwrite('lab.jpg', lab)
    elif args.operation == "border_color":
        COLOR= [b,g,r]
        constant= cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=COLOR)
        cv.imshow("border",constant)
        cv.imwrite("border.jpg",constant)


    cv.waitKey(0)

if __name__ == '__main__':
    main()
