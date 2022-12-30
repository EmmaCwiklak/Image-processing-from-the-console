import cv2

def proba():
    print("Proba udana")

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)