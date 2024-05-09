import cv2 as cv

# img = cv.imread('archive/train/apple/Image_1.jpg')
# cv.imshow('Im', img)

def rescalerFrame(frame, scale=0.2):                   # works for Images, Videos, and Live video
    width = int(frame.shape[1] * scale)           # index 1,0        means width and height respectively
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def chageRes(width,height):       # works only for Live Video
    capture.set(3,width)
    capture.set(4,height)

# resized_image = rescalerFrame(img)
# cv.imshow('Image', resized_image)

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()    

    frame_resized = rescalerFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()                       
cv.destroyAllWindows()              