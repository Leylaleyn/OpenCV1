import cv2
# not göz algılamak istersek önce yüzleri daha sonra gözleri bulmamız gerekecektir

img = cv2.imread("eye.png")

face_cascade = cv2.CascadeClassifier("frontalface.xml")
eye_cascade = cv2.CascadeClassifier("eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)

img2 = img[y:y+h, x:x+w] # aldıgımız değerleri bir nesneye atıyoruz
gray2 = gray[y:y+h, x:x+w]

# yüzü buldum şimdi yüzdeki gözleri bulmalıyım
eyes = eye_cascade.detectMultiScale(gray2)

for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2, (ex,ey), (ex+ew, ew+eh), (255,0,0),2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



