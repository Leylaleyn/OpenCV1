import cv2
import numpy as np

img = cv2.imread("morp.png",0)
# Yeni boyutları belirle
new_width = 400
new_height = 300

# Yeniden boyutlandır
img = cv2.resize(img, (new_width, new_height))

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel, iterations=1)


cv2.imshow("img", img)
cv2.imshow("erosion", erosion)
dilation = cv2.dilate(img,kernel, iterations=1)
cv2.imshow("dilation", dilation)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) # gürültü siliyor
cv2.imshow("opening", opening)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing", closing)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("gradient", gradient)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("tophat", tophat)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()