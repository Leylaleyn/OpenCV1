import cv2

# resim okuma
img = cv2.imread("../Goruntulerile_Temelİslemler/klon.jpg", 0)  # 0 gri tonlarda olsun diye
# print(img)
# img = cv2.resize(img, (640, 480)) resmi yeniden boyutlandırma

# pencere oluşturma
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

# resimleri görme
cv2.imshow("image", img)


# resmi kaydetme
cv2.imwrite("klon1.jpg", img)


cv2.waitKey(0)
cv2.destroyAllWindows()



