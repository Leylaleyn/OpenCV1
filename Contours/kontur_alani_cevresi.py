import cv2

img = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127,255,cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Alan
cnt = contours[0]
area = cv2.contourArea(cnt) # contourArea kullanarak alan bulduk
print(area)
M = cv2.moments(cnt) # moments metodunu kullanarak da alan bulabildik
print(M["m00"])

# Çevre
perimeter = cv2.arcLength(cnt, True) # True -> şeklin kapalı ya da açık olma durumunu belirtiyor true->şekil kapalı
print(perimeter)


"""
cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("thresh",thresh)"""

cv2.waitKey(0)
cv2.destroyAllWindows()





