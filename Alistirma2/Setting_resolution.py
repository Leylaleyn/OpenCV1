# cap.get ve cap.set metodlarını öğreneceğiz
import cv2
import numpy as np

windowName = "Live Video"
cv2.namedWindow(windowName)


cap = cv2.VideoCapture(0)

print("Width : " + str(cap.get(3))) # cap.get(3) -> cap'deki görüntünün enini verir
print("Height : " + str(cap.get(4))) # cap.get(4) -> cap'deki görüntünün yüksekliğini verir

# eni ve yüksekliği değiştirme
cap.set(3, 1280)
cap.set(4, 720)


while True:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow(windowName,frame)


    if cv2.waitKey(1) == 27 :
        break


cap.release()
cv2.destroyAllWindows()






