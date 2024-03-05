# Kontur nedir ?
# Şeklin sınırları boyunca ard arda devam eden ve benzer renk özelliğine sahip olan noktalar bütünüdür

#Temel Kontur tespit algoritması

# Yüksek doğruluklu kontur çizimleri için binary resimler kullanmalıyız: cv2.cvtColor(), cv2.treshold()
# Kontur koordinatlarının tespiti : cv2.findContours
# Bulunan noktaların çizimi : cv2.drawContours()

# Convex Hull : İç bükey şekillere dış bükey örtüler çizmek.

import cv2
import numpy as np

"""
img = cv2.imread("contour1.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY) 

# buradaki 127: Eşik değeridir.Bu değer, bir pikselin yoğunluğunun bu eşik değerinden büyük veya eşit olup olmadığını kontrol etmek için kullanılır. 
# 255: Maksimum değerdir. Eşik değerini aşan piksellerin değeri bu maksimum değere (beyaz renk) ayarlanır.
# cv2.THRESH_BINARY: Bu, eşikleme türünü belirten bir bayraktır. cv2.THRESH_BINARY, bir pikselin değeri eşik değerinden büyükse, yeni değeri maksimum değer olacak şekilde ayarlar.
# Eğer eşik değerinden küçükse, değeri sıfır olacaktır.
# Sonuç olarak, thresh değişkeni, eşikleme işlemine tabi tutulmuş siyah-beyaz (binary) bir görüntüyü içerir.
 Eşikleme işlemi, genellikle nesne tespiti, kenar algılama ve diğer görüntü işleme görevlerinde kullanılır.
# Not
# Bu kod satırı, bir gri tonlamalı görüntüyü eşikleme (thresholding) işlemine tabi tutar. 
# Thresholding işlemi, bir pikselin yoğunluğunu belirli bir eşik değeri ile karşılaştırarak,
# bu eşik değerini aşan pikselleri bir renge, aşmayanları ise başka bir renge dönüştürür. Buradaki '_' ifadesi,
# Python'da kullanılan bir değişken adıdır ve genellikle kullanılmayan bir değişkeni temsil eder.

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# contours : bize kontur koordinatlarını verir print(contours) yaparak da koordinatları inceleyebiliriz

cv2.drawContours(img, contours, -1, (0,0,255), 3)

cv2.imshow("contour", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#nesnelerin izini sürmek

cap = cv2.VideoCapture("dog.mp4")

while(1):
    _, frame = cap.read()
    frame  = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # nesnelerin izini sürmek için hsv renk kodlarını kullanıyoruz

    sensitivity = 15
    lower_white = np.array([0,0,255-sensitivity])  # google'dan araştırılıp bulunabilir, hsv code for blue.. gibi aratabiliriz
    upper_white = np.array([255,sensitivity,255])

    mask = cv2.inRange(hsv, lower_white, upper_white) # hsv'ye çevirdiğim frame'lerin içerisinden lower white ve upper white arasında olan yere maske uygula geri kalanı sil, kazı
    res = cv2.bitwise_and(frame, frame,mask = mask) #mask'ın doğru uygulanabilmesi için, google dan bak

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    if cv2.waitKey(10) & 0xFF == ord("q"):  # her frame 30 sn gösterilecek
        break

cv2.destroyAllWindows()


