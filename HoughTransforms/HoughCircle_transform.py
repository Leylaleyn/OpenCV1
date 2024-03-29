
import cv2
import numpy as np

img1 = cv2.imread("coins.jpg")
img2 = cv2.imread("balls.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#gürültüleri yok edelim

img1_blur = cv2.medianBlur(gray1,5) # kernel size : 5 (not:tek sayı olmalı çift olmamalı)
img2_blur = cv2.medianBlur(gray2,5)

circles = cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1 = 200,param2 = 10, minRadius = 15, maxRadius = 90) # (img,algılama yöntemimiz, çözünürlük oranı, circle ler arasındaki min mesafe (img1.shape[0]/64) genelde bu kullanılır,param1, param2 değişkenleri bu metoda özel parametrelerdir)


if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img1, (i[0],i[1]), i[2], (0,255,0), 2)


cv2.imshow("IMG1",img1)


cv2.waitKey(0)
cv2.destroyAllWindows()





