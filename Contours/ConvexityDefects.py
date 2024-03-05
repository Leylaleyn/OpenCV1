# Dış Bükey Kusurlar
import cv2
import numpy as np

img = cv2.imread("star.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, 0) # Gri tonlamalı görüntü üzerine eşikleme işlemi uygulanır. Bu işlem, görüntüyü siyah-beyaz hale getirir.

contours, _ = cv2.findContours(thresh,2,1) # Eşikleme sonrası görüntü üzerindeki konturlar (contours) bulunur.

cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints = False) # returnPoints -> False : convexHull'dan gelen değerlerin indislerini dönüyor(kendileri değil)
# İlk kontur alınır ve bu konturun konveks kabuğu (hull) hesaplanır. returnPoints=False parametresi, konveks kabuğun indekslerini döndürmesini sağlar.

defects = cv2.convexityDefects(cnt,hull)
# Konveks kusurlar (defects) hesaplanır. Bu, konturun konveks kabuğu ile arasındaki farklardır.

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]  # s:başlangıç, e: bitiş noktası, f: en uzak nokta, d: uzaklık
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])  # far iç büküm noktaları

    cv2.line(img,start,end, [0,255,0],2)
    cv2.circle(img,far,5,[0,255,0],-1)








cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()











