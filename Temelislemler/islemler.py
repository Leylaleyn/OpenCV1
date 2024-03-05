
# Resimlerde toplama işlemi yapabilmek için aynı boyutta olmaları gerekir çünkü resimlerde bir matristir
# ve matrislerde toplama yapabilmemiz için aynı boyutta olması gerekir

import cv2
import numpy as np

circle = np.zeros((512,512,3), np.uint8) + 255
cv2.circle(circle, (256,256), radius=60, color=(255,0,0), thickness=-1)

rectangle = np.zeros((512,512,3), np.uint8) + 255
cv2.rectangle(rectangle, (150,150), (350,350), color=(0,0,210), thickness=-1)

# oluşturduğumuz bu resimleri toplayalım
add = cv2.add(circle,rectangle)
"""
cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Add", add)


"""


######## AĞIRLIKLI TOPLAMA  #########

# f(x,y) = x*a + y*b + c

dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0) # addWeighted(circle, 0.7 yogunlukta circle dan, rectangle, 0.3 yogunlukta rectangle dan, 0:sabit sayı)

cv2.imshow("Dst", dst)



cv2.waitKey(0)
cv2.destroyAllWindows()