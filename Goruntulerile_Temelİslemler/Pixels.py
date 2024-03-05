import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("opencv.png")

px = img1[10, 10]
print(px)

(b, g, r) = img1[150, 30]
print("Red : {}, Green: {}, Blue: {}".format(r,g,b))
######################################
img = cv2.imread("forest.jpg")

# belirli bir bölgenin renginde değişiklik yapmak istersek

corner = img[0:100, 0:100]
corner_1 = img[0:100, 0:250]  # [y_start : y_end, x_start : x_end]

cv2.imshow("Corner",corner)
cv2.imshow("Corner-1",corner_1)
cv2.namedWindow("Forest",cv2.WINDOW_NORMAL)
cv2.imshow("Forest", img)

# rengi değiştirelim

img[0:100, 0:250] = (255,0,0) #böyle sayıları kafamıza göre veriyoruz ama resin boyutunu bilmemiz gerekir
cv2.imshow("Değiştirilmiş Görüntü", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
