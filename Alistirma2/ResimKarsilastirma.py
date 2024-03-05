import cv2
import numpy as np

img1 = cv2.imread("aircraft.jpg")
img1 = cv2.resize(img1,(500,500))

img2 = cv2.imread("aircraft1.jpg")
img2 = cv2.resize(img2,(500,500))

img3 = cv2.medianBlur(img1,7) # karşılaştıralım

# resimlerin aynı olması için boyutlarının da aynı olması gerekiyor, bu yüzden önceden boyutlarını bilsek bizim için daha iyi olur

if img1.shape == img2.shape:
    print("same size")
else:
    print("not same")

diff = cv2.subtract(img1, img3)

cv2.imshow("Difference",diff) # hiçbir fark bulamadı bu yüzden simsiyah bir ekran verdi
b,g,r = cv2.split(diff) # daha iyi anlaşılabilmesi için diff'in bgr değerlerine baktık
# print(b)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0: # sıfır olmayan değerleri sayar
    print("completely equal")
else:
    print("NOT completely equal")



#cv2.imshow("Aircraft",img1)
#cv2.imshow("Aircraft1",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()