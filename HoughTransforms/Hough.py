# Hough dönüşümü, özellikle doğru ve düz çizgilerin tespiti için kullanılan bir görüntü işleme tekniğidir.

import cv2
import numpy as np

####################### RESİMLER ÜZERİNDE ÇİZGİLERİ ALGILAMA #############################
"""
img = cv2.imread("h_line.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,75,150) # Canny(img, min değer, max değer)

# cv2.HoughLines() # ikisinin de görevi benzer fakat bu daha çok CPU kullanıyor bilgisayarı daha çok yoruyor
lines = cv2.HoughLinesP(edges,1,np.pi/180,30, maxLineGap = 120) # HoughLinesP(kenarları tespit edilmiş img, rho, theta değeri, treshold değeri) macLineGap : boşlukları dolduruyor
# bu değerlerin anlamı notlarımda açıklanmıştır
print(lines)
# direkt cv2.imshow ile çekemiyoruz, döngü kurmamız gerekir

for line in lines:
    x1,y1,x2,y2 = line[0] # x1,y1 çizgimizin başlangıç değerleri x2,y2 bitiş değerleri
    cv2.line(img,(x1,y1),(x2,y2),(0,255,255),2)

cv2.imshow("Img",img)
cv2.imshow("Gray",gray)
cv2.imshow("edges",edges)
cv2.waitKey(0)
"""
############################## VİDEOLAR ÜZERİNDE ÇİZGİLERİ ALGILAMA #############################
# görüntüdeki sarı çizgileri tespit etmeyi amaçlıyoruz
vid = cv2.VideoCapture("line.mp4")

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame,(630,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([18,94,140], np.uint8)  # hsv range for yellow
    upper_yellow = np.array([48, 255, 255], np.uint8)

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    edges = cv2.Canny(mask,75,250)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=70)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        print(lines) #[[[354 325 490 476]] ifadesi bir çizgiyi temsil eder. Bu çizginin başlangıç noktası (x1, y1) = (354, 325) ve bitiş noktası (x2, y2) = (490, 476) olarak belirlenmiştir.


    #cv2.imshow("mask",mask)
    #cv2.imshow("edges",edges)
    cv2.imshow("Img",frame)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()


cv2.destroyAllWindows()


