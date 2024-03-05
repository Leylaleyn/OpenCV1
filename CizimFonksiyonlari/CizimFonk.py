import cv2
import numpy as np

# canvas = np.zeros((512,512,3), dtype=np.uint8)  #beyaza çevirmek için + 255 diyebiliriz
## print(canvas)  0'lardan oluşan matris



"""
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()  """

"""
## Bilgisayarlar bir görüntüyü Nasıl Oluşturur ?

import numpy as np
import cv2

img2 = np.zeros((10, 10, 3), np.uint8)
img2[0, 0] = (255, 255, 255)
img2[0, 1] = (255, 255, 200)
img2[0, 2] = (255, 255, 150)
img2[0, 3] = (255, 255, 15)

# 'cv2.resize' fonksiyonunu kullanarak boyutu değiştirin
resized_img = cv2.resize(img2, (1000, 1000), interpolation=cv2.INTER_AREA)

cv2.imshow("Canvas", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()   """

# Cizim Fonksiyonları

canvas = np.zeros((512,512,3), dtype=np.uint8)

cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5)  # başlangıç noktası : (50,50), bitiş noktası : (512,512), rgb : (255,0,0), kalınlık=5
cv2.line(canvas, (100,50), (200,250), (25,120,130), thickness=3)

# dikdörtgen
cv2.rectangle(canvas, (20,20), (50,50), (0,214,123), thickness=-1)  # sol üst köşe ve sağ alt köşe koordinatlarına ihtiyacımız olacak
cv2.rectangle(canvas, (50,500), (150,150), (0,214,0), thickness=2)

#çember
cv2.circle(canvas, (250,250), 100, (120,124,44), thickness=5)  # merkez, yarıçap, renk, kalınlık

# üçgen çizimi
p1 = (100, 200)
p2 = (50,50)
p3 = (300,100)

cv2.line(canvas, p1, p2, (123,123,123), 3)
cv2.line(canvas, p2, p3, (123,123,123), 3)
cv2.line(canvas, p1, p3, (123,123,123), 3)


#ya da
"""
# Üçgenin üç köşe noktası
pts = np.array([[400, 50], [300, 200], [500, 200]], np.int32)
pts = pts.reshape((-1, 1, 2))
# Üçgeni çiz
cv2.polylines(canvas, [pts], isClosed=True, color=(0, 255, 0), thickness=3)
"""

# biçok şekiller

points = np.array([[[110,200], [330,200], [190,220], [220,250]]], np.int32)
cv2.polylines(canvas, [points], True, (0,0,100), 5)  # kapalı olmasını istiyorsak = True

# elipse
cv2.ellipse(canvas, (300,300), (80,20), 10, 0, 360, (211,211,45),-1) # elipsin merkezi, (Genişlik, yükseklik),yatay eksende yapacağı açı = 10, başlangıç = 90 ve bitiş = 360 açısı

"""
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows() """

# YAZI YAZDIRMA

canvas2 = np.zeros((512,512,3), dtype=np.uint8) + 255

# yazı tipleri
font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_SIMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas2, "OpenCV", (30,140), font3, 5, (0,0,123), cv2.LINE_AA )  # ( canvas, yazılacak_metin, koordinatları(metnin sol alt koordinatı), font, fontun_büyüklügü, renk, yazı tipi)

"""
cv2.imshow("Canvas2",canvas2)
cv2.waitKey(0)
cv2.destroyAllWindows()"""


# TRACKBAR
"""
buradavOpenCV ile birlikte kullanılan bir trackbar arayüzünü açıklar.
 Bu arayüz, bir görüntü üzerinde renk değerlerini (kırmızı, yeşil, mavi) ve bir anahtar anahtarı (switch) 
 kullanarak değiştirmenize olanak tanır. Bu tür trackbarlar, özellikle renk değerlerini veya diğer parametreleri 
 canlı bir şekilde ayarlamak için kullanışlıdır."""
def nothing(x):
    pass

img = np.zeros((512,512,3), dtype=np.uint8)
cv2.namedWindow("image") # trackbar arayüzünü bu rengini değiştireceğimiz pencereye yerleştiriceğimizi belirtnek için ad verdik

cv2.createTrackbar("R", "image", 0, 255, nothing) # opencv nin kullanım şeklinden kaynaklı bu trackbar içerisine boş bir fonk tanımlamamız gerekiyormuş
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
switch = "0: OFF, 1:ON"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

"""while Döngüsü: Trackbar'ların konumlarını sürekli olarak güncellemek ve görüntüyü göstermek için bir döngü başlatılır."""
while True: # trackbarlarımızın konumlarını sürekli değiştirdiğimiz için bir while döngüsü içerisinde yazmalıyız
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")

    if s == 0:
        img[:] == [0, 0, 0]
    if s == 1:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
