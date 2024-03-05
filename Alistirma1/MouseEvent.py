import cv2

cap = cv2.VideoCapture("line.mp4")

circles = []

def mouse(event,x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN: #sol tuşa bastığımda aşağıdaki işlemleri yap demek
        circles.append((x,y))


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse) # nerede yapılacak(pencere), yapılan işlem nedir bunları belirlememiz gerekiyor

while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame, (640,480))

    for center in circles: # merkezler üzerinden çember çiziyoruz
        cv2.circle(frame, center, 20, (255,0,0), -1)

    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)

    if key == 27: # esc ye bastıysak çık
        break

    elif key == ord("h"): #h tuşuna bastığında pencereyi temizlesin
        circles = []

cap.release()
cv2.destroyAllWindows()









