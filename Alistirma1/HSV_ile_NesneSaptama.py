# daha iyi sonuçlar verdi
import cv2
import numpy as np

def nothing(x):  # hsv'de hata almamak için
    pass

cap = cv2.VideoCapture(0)


cv2.namedWindow("Trackbar")

cv2.createTrackbar("Lower - H", "Trackbar",0,179, nothing)
cv2.createTrackbar("Lower - S", "Trackbar",0,255, nothing)
cv2.createTrackbar("Lower - V", "Trackbar",0,255, nothing)
cv2.createTrackbar("Upper - H", "Trackbar",0,180, nothing)
cv2.createTrackbar("Upper - S", "Trackbar",0,255, nothing)
cv2.createTrackbar("Upper - V", "Trackbar",0,255, nothing)

while 1:

    _, frame = cap.read()
    frame = cv2.flip(frame,1)

    frame = cv2.resize(frame, (500,350))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("Lower - H", "Trackbar")
    ls = cv2.getTrackbarPos("Lower - S", "Trackbar")
    lv = cv2.getTrackbarPos("Lower - V", "Trackbar")
    uh = cv2.getTrackbarPos("Upper - H", "Trackbar")
    us = cv2.getTrackbarPos("Upper - S", "Trackbar")
    uv = cv2.getTrackbarPos("Upper - V", "Trackbar")

    lower_blue = np.array([lh,ls,lv])
    upper_blue = np.array([uh,uv,us])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    bitwise = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()