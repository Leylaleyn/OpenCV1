# Plaka olan yer bizim görüntülemek istediğimiz tek yer geri kalan yerleri gürültü olarak kabul ediyoruz

# Önce algoritmayı anlayalım
# 1) İlk olarak resmi gri tonlara çeviriyoruz cv2.cvtColor()
# 2) Daha sonra gri tonlara çevirdiğimiz resmin köşelerini yumuşatmamız gerekiyor cv2.bilateralFilter() burada plaka dışındaki her yeri
# gürültü kabul etmek istiyoruz
# 3) Canny yöntemiyle köşeleri tespit ediyoruz cv2.Canny()
# 4) Plakanın konturlarını elde ediyoruz
# 5) Tespit ettiğimiz plakaya mask uygulayıp kırpıyoruz
# 6) en son pytesseract ile metnimizi okuyoruz


import cv2
import numpy as np
import pytesseract
import imutils

# Görüntü okuma
img = cv2.imread("car.jpg")
# Gri Tonlama
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Gürültü azaltma
filtered = cv2.bilateralFilter(gray,6,250,250)
# Kenar Tespiti
edged = cv2.Canny(filtered, 30, 200)

# Kontur bulma
"""cv2.findContours() fonksiyonu kullanılarak kenarlıkların kontürleri bulunur. 
Ardından imutils.grab_contours() yardımcı işlevi ile kontur listesi alınır ve 
alanlarına göre sıralanır."""

contours = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # contours koordinatları tutuyor
cnts = imutils.grab_contours(contours) # contours değişkenindeki uygun değerleri yakalıyor
# koordinatlara bakarak dikdörtgen şeklinde kapalı bir alan arıyoruz, ard arda sıralanmı noktalara bakıyoruz eğer bir dikdörtgen oluşturmuşsa burada dikdörtgen var diyorum
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10] #girdiğim cnts değerlerinini alana göre sıraladık
screen = None

"""Plaka Tespiti:
Konturlar arasından döngü oluşturularak, yaklaşık 4 köşeye sahip olan kontur bulunur
. Bu, potansiyel olarak araç plakasına karşılık gelecek bir kontur bulmamızı sağlar."""
# Şimdi kapalı bir şekil arayacağız
for c in cnts:
    epsilon = 0.018*cv2.arcLength(c,True) # arcLength konturlerin yay uzunluğunu bulur
    approx = cv2.approxPolyDP(c,epsilon,True) # (koordinatlar, epsilon katsayısı, True)
    if len(approx) == 4: # 4 koşe tespit edildiyse, bu bir dikdörtgendir
        screen = approx
        break
# Maskeleme İşlemi
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask,[screen],0,(255,255,255),-1) # plaka bolgesiini beyaza çeviriyoruz, geri kalan yerler siyah
new_img = cv2.bitwise_and(img, img, mask = mask)

# Kırpma işlemi
(x,y) = np.where(mask == 255) #mask da beyaz olan yerlerin koordinatlarını al ve bunları sakla
(topx, topy) = (np.min(x), np.min(y)) # bilgisayarda en üst nokta 0,0 dır o yüzden min dedik
(bottomx, bottomy) = (np.max(x), np.max(y))
cropped = gray[topx:bottomx+1, topy:bottomy+1]

# metni okuma
text = pytesseract.image_to_string(cropped, lang="eng")
print("detected text:", text)

cv2.imshow('original', img)
# cv2.imshow('gray', gray)
# cv2.imshow('Yumusatma', filtered)
# cv2.imshow('edged', edged)
cv2.imshow('mask', new_img)
cv2.imshow("Cropped",cropped)




cv2.waitKey(0)
cv2.destroyAllWindows()





