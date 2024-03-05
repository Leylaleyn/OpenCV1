import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("opencv.png")
print("Shape: ", img.shape)

(B, G, R) = cv2.split(img)
merged = cv2.merge([B, G, R]) # split ettiğimiz görüntüleri birleştirmek istersek

"""
cv2.imshow("OpenCV-Merged", merged)

cv2.imshow("OpenCV-B", B) #blue yu çıkarıyor
cv2.imshow("OpenCV-G", G) # green i çıkarıyor
cv2.imshow("OpenCV-R", R) # red i çıkarıyor
"""
# split ettğimiz metodları daha net bir şekilde incelemek istersek
black = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([black,black,R])) # kırımızı renk dışındakileri siyaha boyamışız
cv2.imshow("Green", cv2.merge([black,G,black]))
cv2.imshow("Blue", cv2.merge([B,black,black]))




cv2.imshow("OpenCV", img)
cv2.waitKey(0)
cv2.destroyAllWindows()