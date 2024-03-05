import cv2
import numpy as np

img = cv2.imread("text.png")
img1 = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 500, 0.01, 10)  # (gray, max köşe sayısı, kalite değeri = 0.01, köşeler arası min distance )
"""
cv2.goodFeaturesToTrack(): Giriş resmindeki iyi köşeleri tespit eder. 
Bu işlev, Shi-Tomasi köşe algılama yöntemini kullanır. 500 köşe bulunmasını ister. 
0.01 değeri, köşe kalitesi parametresidir. Bu değer ne kadar yüksekse, o kadar iyi kaliteli köşeler alınır. 
10 ise minimum euclidean mesafesini belirtir, yani köşeler arasındaki minimum mesafeyi belirler.
 """

corners = np.intp(corners)  #çemberler çizerken float tipinde kullanamıyoruz

for corner in corners:
    x,y = corner.ravel() # x ve y değerlerini daha rahat alabilmek için ravel metodunu giriyorum (ravel tek bir satır haline getiriyor)
    cv2.circle(img, (x,y),3,(0,0,255),-1)

cv2.imshow("corner", img)

cv2.waitKey(0)
cv2.destroyAllWindows()








