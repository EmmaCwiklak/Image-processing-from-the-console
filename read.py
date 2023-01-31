import cv2 as cv
import argparse
from functions import rescaleFrame, resizing, gray, blur, canny

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='cat.jpg', help='path to your picture')
    parser.add_argument("--operation", default='default', help='choose edit operation')
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


    if args.operation == "default":
        # wyswietlanie obrazu
        if args.x != 5:
            rescaleFrame(img, x)
        else:
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

    elif args.operation == "split":
        merged = cv.merge([b,g,r])
        cv.imshow("Merged Image", merged)

    cv.waitKey(0)

if __name__ == '__main__':
    main()


