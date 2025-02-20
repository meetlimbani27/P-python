import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=70, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHands(self, img, draw= True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB format
        results = self.hands.process(imgRGB)
            #  print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                     self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
                # for id, lm in enumerate(handLms.landmark):
                #         # print(id, lm)
                #     h, w, c = img.shape
                #     cx, cy = int(lm.x * w), int(lm.y * h)
                #     print(id, cx, cy)
                #     if id == 0:
                #         cv2.circle(img, (cx, cy),15 ,(255, 0, 255), cv2.FILLED)
             

def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to read a frame from the camera.")
            break
        img = detector.findHands(img)

        cTime = time.time()
        fps = 1/ (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 255), 3)


        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):  # Break the loop and close the camera when 'q' is pressed
            break
    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all windows
     


if __name__ == "__main__":
    main()