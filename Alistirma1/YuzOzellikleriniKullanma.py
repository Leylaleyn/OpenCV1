import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

# Bu fonksiyon, verilen kontur listesinden maksimum alana sahip olanı bulur ve döndürür.
def findMaxContour(contours):
    max_i = 0
    max_area = 0

    for i in range(len(contours)): #alanları birbiriyle karşılaştırarak max olanı bulmaya çalışacak
        area_face = cv2.contourArea(contours[i])

        if max_area < area_face:
            max_area = area_face
            max_i = i

        try:
            c = contours[max_i] # maksimum i indeksindeki kontur değerini tutacak

        except:
            contours = [0] # eğer bulamazsa contour değerimiz 0 olsun
            c = contours[0]

        return c
while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    roi = frame[50:250, 200:400] # frame[y1:y2, x1:x2]

    cv2.rectangle(frame, (200,50), (400,250), (0,0,255), 0) # pencere, başladığı nokta, sağ alt noktası, renk değeri, kalınlık

    # yüzümü diğer bölgelerden ayırabilmek için görüntümü hsv formatına çevireceğim

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower_color = np.array([115,22,77], dtype=np.uint8)
    upper_color = np.array([180,255,255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_color, upper_color) # Belirli bir renk aralığını maskelemek için cv2.inRange() kullanılır.

# Ardından, maskeyi iyileştirmek için bir dizi morfolojik işlem (genişletme, blur vb.) uyguluyoruz.
    # beyaz içindeki siyah karıncalanmaları yok etmek istiyoruz
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.medianBlur(mask, 15)

    # Görüntü içerisinde kontur arayalım
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:

        try:  # beyaz karıncalanmalarla ilgilenmek istemediğimizden, yüzüm o roi'deki max konture sahip nesne olacak
            c = findMaxContour(contours) # max konturun tutulduğu değer
            extLeft = tuple(c[c[:, :, 0].argmin()][0]) # x'in en küçük olduğu yer
            extRight = tuple(c[c[:, :, 0].argmax()][0]) # x'in en büyük old yer
            extTop = tuple(c[c[:, :, 1].argmin()][0]) # y'nin en küçük old yer
            extBot = tuple(c[c[:, :, 1].argmin()][0]) #y'nin en büyük old yer

            cv2.circle(roi, extLeft, 5, (0,255,0), 2)
            cv2.circle(roi, extRight, 5, (0,255,0), 2)
            cv2.circle(roi, extTop, 5, (0,255,0), 2)
            cv2.circle(roi, extBot, 5, (0,255,0), 2)

            cv2.line(roi, extLeft, extTop, (255,0,0),2)
            cv2.line(roi, extTop, extRight, (255,0,0),2)
            cv2.line(roi, extRight, extBot, (255,0,0),2)
            cv2.line(roi, extBot, extLeft, (255,0,0),2)

            # AÇI BULMA
            # önce kenar uzunluklarını bulalım (x1-x2)^2 + (y1,y2)^2
            a = math.sqrt((extRight[0] - extTop[0])**2 + (extRight[1] - extTop[1]) **2)
            b = math.sqrt((extBot[0] - extRight[0])**2 + (extBot[1] - extRight[1]) **2)
            c = math.sqrt((extBot[0] - extTop[0])**2 + (extBot[1] - extTop[1]) **2)

    # Ardından, üçgen formülü kullanılarak dönme açısı hesaplanır ve ROI içine yazdırılır.
            try:
                angle_ab = math.acos((c**2 + b**2 - a**2)/(2*b*a))*57 # 0'a bölünme hatası alma ihtimalinden try except içinde yazdık
                cv2.putText(roi, str(angle_ab), (extRight[0] - 50, extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2, cv2.LINE_AA )

            except:
                cv2.putText(roi," ? ", (extRight[0] - 60, extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2, cv2.LINE_AA )



        except:
            pass


    else:
        pass

    cv2.imshow("frame", frame)
    cv2.imshow("roi", roi)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break












cap.release()
cv2.destroyAllWindows()

