import cv2
import numpy as np

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")

bit_and = cv2.bitwise_and(img2, img1)  # Ve bağlacı kullanıyoruz 0 ve 1 karşılaştırdığımızda 0 baskın gelir
#cv2.imshow("bit and", bit_and)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

bit_or = cv2.bitwise_or(img2, img1)  # Or bağlacı kullanıyoruz 0 ve 1 karşılaştırdığımızda 1 baskın gelir
# cv2.imshow("bit and", bit_or)

bit_xor = cv2.bitwise_xor(img2,img1)  # 0-1 -> 0,   1-1, 0-0 ->1 AYNI OLANLAR 1 farklı olanlar 0
bit_not = cv2.bitwise_not(img2)  # not tam tersi rengine çeviriyor
bit_not2 = cv2.bitwise_not(img1) #

cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)
cv2.imshow("bit_not2", bit_not2)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""
# Resim Dönüşüm Dizeyi 
import cv2
import numpy as np

img = cv2.imread("helikopter.jpg",0)
row,col = img.shape

M= np.float32([[1,0,50],[0,1,200]])

dst = cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)

"""
"""
#Resmi Döndürme
import cv2
import numpy as np

img = cv2.imread("helikopter.jpg",0)
row,col = img.shape

M= cv2.getRotationMatrix2D((col/2,row/3),180,1) # resmi 180 derece döndürdü

dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)

"""