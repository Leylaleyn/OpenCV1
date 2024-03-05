# Resimler veya videolar üzerindeki hedeflenen nesnelerin algılanmasında kullanılır.
# haar light denilen siyah beyaz pixellerden oluşan özellikleri vardır
# https://github.com/opencv/opencv/tree/master/data/haarcascades

###### ADIMLAR ######
# 1) İlgili kütüphaneyi, görüntüyü ve haar cascade dosyasına dahil et
# 2) Görüntüyü boz(gri) tonlara çevirerek üzerinde ilgili nesneyi ara
# 3) Bulunan nesneyi işaretle

# Not: cascade dosyamız gray tonlarında nesneyi daha iyi bulur

import cv2
img = cv2.imread("face.png")

face_cascade = cv2.CascadeClassifier("frontalface.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.3, 6)  #cascade dosyasını kullanıp bana yüzlerin koordinatlarını bul diyorum
# 1.3 = ölçeklendirme değeri, 4 = belirli bir bölgede kaç farklı pencerenin yüz bulmasını istediğimiz sayı
# belirli bir bolgede en az 4 pencere yüz bulsun ki ben orda yüz bulunduğundan emin olayım

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2) #sol üst ve sağ alt koordinatları

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




















