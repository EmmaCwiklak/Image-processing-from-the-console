import cv2 as cv

def rescaleFrame(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)

    img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
    return cv.imshow('default', img)
def resizing(img, scale_percent):
    print('Original Dimensions : ', img.shape)

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

    print('Resized Dimensions : ', resized.shape)

    cv.imshow("Resized image", resized)
    cv.waitKey(0)

    cv.imwrite('resize.jpg', resized)
def gray(img):
    image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', image)
    cv.imwrite('gray.jpg', image)
def blur(img,x):
    image = cv.GaussianBlur(img, (x,x), cv.BORDER_DEFAULT)
    cv.imshow('Blur', image)
    cv.imwrite('blur.jpg', image)
def canny(img):
    image = cv.Canny(img, 125, 175)
    cv.imshow('Canny', image)
    cv.imwrite('canny.jpg', image)

#def filtrowanie_koloru(img):
