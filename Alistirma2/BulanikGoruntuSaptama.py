import cv2

img = cv2.imread("starwars.jpg")

blurry_img = cv2.medianBlur(img, 7)

laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()
laplacian2 = cv2.Laplacian(img, cv2.CV_64F).var()

print(laplacian)
print(laplacian2)

if laplacian < 500:
    print("blurry image ")

    # yani laplacian değeri azalırsa bulanıklık artar

cv2.imshow("img",img)
cv2.imshow("blurry img",blurry_img)


cv2.waitKey(0)
cv2.destroyAllWindows()





