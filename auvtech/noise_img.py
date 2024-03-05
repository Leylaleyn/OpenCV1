import cv2
import numpy as np
from matplotlib import pyplot as plt

# Görüntüyü yükle
img = cv2.imread('sualti.png')
"""
# Gaussian Blur uygula
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Median Blur uygula
median_blurred_image = cv2.medianBlur(image, 5)

# Bilateral Filter uygula
bilateral_filtered_image = cv2.bilateralFilter(image, 9, 75, 75)

# Sonuçları göster
cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blur', blurred_image)
cv2.imshow('Median Blur', median_blurred_image)
cv2.imshow('Bilateral Filter', bilateral_filtered_image)
"""
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()
