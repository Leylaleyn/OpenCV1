import cv2


img = cv2.imread("contour.png")
# Gri tonlamaya çevir
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Binarizasyon
_, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

M = cv2.moments(thresh) # img feature değerlerini çekmek istersek
# print(M)  #sözlük türünde m10, m00, m01 değerleri...

#Geometri merkezinin koordinatlari
X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])

# ağırlık merkezine yuvarlak çizelim
cv2.circle(img,(X,Y),5,(255,0,255),-1)

cv2.imshow("img",img)


cv2.waitKey(0)
cv2.destroyAllWindows()












