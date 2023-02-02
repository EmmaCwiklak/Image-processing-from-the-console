import cv2 as cv
import numpy as np
import argparse
from functions import rescaleFrame, resizing, gray, blur, canny, translate, rotate,test

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='wsb.jpg', help='path to your picture')
    parser.add_argument("--operation", default='default', help='choose edit operation', choices=["resize","gray","blur", "canny" , "translate", "rotate","flip", "border_color", "lab", "hsv", "cutsmth"])
    parser.add_argument("--x", help='x parameter', default=0.5, type=float)
    parser.add_argument("--y", help='y parameter', default=0.5, type=float)
    parser.add_argument("--r", help='red', default=255, type=float, choices=["0-255"])
    parser.add_argument("--g", help='green', default=255, type=float, choices=["0-255"])
    parser.add_argument("--b", help='blue', default=255, type=float, choices=["0-255"])
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
        rescaleFrame(img, 1)

    elif args.operation == "resize":
        resizing(img,x)

    elif args.operation == "cutsmth":
        cv.imshow("Oryginal",img)
        img = img[0:x, 0:y, :]
        cv.imshow('Cutted', img)
        cv.imwrite('cut.jpg', img)

    elif args.operation == "gray":
        gray(img)
        file = "gray.jpg"
        test(file)

    elif args.operation == "blur":
        if x%2==0:
            x+=1
        blur(img,x)

    elif args.operation == "canny":
        canny(img)

    elif args.operation == "translate":
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
