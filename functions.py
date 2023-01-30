import cv2

def rescaleFrame(img, scale=0.75):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(img, dimensions, interpolation=cv2.INTER_AREA)

def resizing(img):
    image = cv2.imread(img)

    print('Original Dimensions : ', image.shape)

    scale_percent = 10  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    print('Resized Dimensions : ', resized.shape)

    img_result= resized.copy()

    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

def gray(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', image)
    return image

def blur(img):
    image = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
    return cv2.imshow('Blur', image)

def canny(img):
    image = cv2.Canny(img, 125, 175)
    return cv2.imshow('Canny', image)

#def filtrowanie_koloru(img):

def obrot(img):
    image = cv2.imread(img)
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    b, g, r = cv2.split(image)
    image = cv2.merge((b, g, r))
    cv2.imshow("Resized image", image)

#wyszarzać, filtrować kolor, zmieniać rozmiar, obracać

