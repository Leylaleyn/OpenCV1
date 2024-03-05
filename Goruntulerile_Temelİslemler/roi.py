######## ROI --> Region of Interest  ( İlgi alanları )
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("basketball.jpg")
print("Shape: ", img.shape)

roi = img[40:150, 120:200] # sadece top gözüksün diye ayarlamalar yaptık

# istersek bu basketbol topunu başka bir yere yapıştırabiliriz

img[20:130, 20:100] = roi # aynı aralıklı ölçü olmasına dikkat edilmeli

cv2.imshow("Basketball ROI", roi)
cv2.imshow("Basketball", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
