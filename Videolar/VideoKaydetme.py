import cv2


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fileName = "C:/Users/Aleyna/PycharmProjects/OpenCV/Videolar/webcam.avi"
codec = cv2.VideoWriter_fourcc('X','V','I','D')
frameRate = 30
resolution = (640,480)
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Webcam Live", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()