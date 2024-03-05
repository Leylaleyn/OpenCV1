import cv2
# not göz algılamak istersek önce yüzleri daha sonra gözleri bulmamız gerekecektir

img = cv2.imread("smile.jpg")
face_cascade = cv2.CascadeClassifier("frontalface.xml")
smile_cascade = cv2.CascadeClassifier("smile.xml")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,x+h),(255,0,255),3)

roi_img = img[y:y+h, x:x+h]
roi_gray = gray[y:y+h, x:x+h]

smiles = smile_cascade.detectMultiScale(roi_gray, 1.5, 5)

for (sx, sy, sw, sh) in smiles:
    cv2.rectangle(roi_img, (sx,sy),(sx+sw, sy+sh), (233,211,23),2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

