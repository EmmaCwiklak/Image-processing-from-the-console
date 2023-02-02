import cv2 as cv
import numpy as np
import filecmp
def rescaleFrame(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)

    img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    return cv.imshow('default', img)

def resizing(img, scale):
    print('Original Dimensions : ', img.shape)

    width = int(img.shape[1] * scale/100)
    height = int(img.shape[0] * scale/100)
    dim = (width, height)

    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    print('Resized Dimensions : ', resized.shape)

    cv.imshow("Resized image", resized)
    cv.waitKey(0)

    cv.imwrite('resize.jpg', resized)
    return resized
def gray(img):
    image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', image)
    cv.imwrite('gray.jpg', image)
    return image

def blur(img,x):
    image = cv.GaussianBlur(img, (x,x), cv.BORDER_DEFAULT)
    cv.imshow('Blur', image)
    cv.imwrite('blur.jpg', image)
def canny(img):
    image = cv.Canny(img, 125, 175)
    cv.imshow('Canny', image)
    cv.imwrite('canny.jpg', image)
def translate(img, x, y):
    image = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, image, dimensions)
    cv.imshow('Translated', image)
    cv.imwrite('translated.jpg', image)
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2, height//2)

    rotated = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotated, dimensions)
    cv.imshow('Rotated', image)

def test(img):
    try:
        filecmp.cmp(img,"gray_wsb.jpg")
    except:
        print("Pliki nie sa takie same")
    else:
        print("Pliki sa takie same")
    finally:
        print("Koniec")
