import cv2 as cv

img = cv.imread('archive/train/apple/Image_1.jpg')           # This function takes path of the image and returns that image as a matrix of pixels
cv.imshow('Apple', img)        # displays the image in a new window , 'Apple' is the name of the window
cv.waitKey(0)            # dosen't let the window diappear,    if image is larger than the windows then it will cut off




"""  For Video
capture = cv.VideoCapture(0)           # to read a video we have to do it frame by frame using while loop , we can pass 0 for webcam or path of the window , capture variable is the instance of the class videocapture
while True:
    isTrue, frame = capture.read()          # this function returns boolean(frame read succesfull or not) and the frame
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()                       #release capture device
cv.destroyAllWindows()                  # -215 error states that the video ran out of frames or the path is not correct
"""



