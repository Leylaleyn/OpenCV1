import cv2
import numpy as np

img = cv2.imread("starwars.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread("starwars2.jpg",0) #aynı şekilde burada da 0 yazarak griye çevirebiliyoruz
h,w= img2.shape[::-1]

result = cv2.matchTemplate(gray_img, img2, cv2.TM_CCOEFF_NORMED) # buraya bakınca aslında match etmek istediğimiz resmin beyaz nokta üzerinde olduğunu anlıyoruz

# dolayısıyla benim result'ım daki değerler ne kadar 1 e yakınsa şablonumumn bulunacağı yer de o kadar yakın olur
location = np.where(result >= 0.9)

for point in zip(*location[::-1]): # [::-1] normalde genişlik ve yüksekliği alırken -1 ile tam tersi yükselik ile genişliği alıyor
    cv2.rectangle(img, point, (point[0] + w, point[1] + h), ( 255,0,0), 3 )



# cv2.imshow("Result",result)
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()