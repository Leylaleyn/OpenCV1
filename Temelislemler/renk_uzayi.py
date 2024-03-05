import cv2
import numpy as np

img = cv2.imread("../Goruntulerile_Temelİslemler/klon.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

"""
cv2.imshow("Klon BGR", img)
cv2.imshow("Klon RGB", img2)
cv2.imshow("Klon HSV", img_hsv)
cv2.imshow("Klon Gray", img_gray)
"""

cap = cv2.VideoCapture("cameraman.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,480))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        break

    cv2.imshow("Video", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()



