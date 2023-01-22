import cv2

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

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

#wyszarzać, filtrować kolor, zmieniać rozmiar, obracać

