import cv2
import numpy as np
import math

vid = cv2.VideoCapture(0)

while(1):
    try:
        ret, frame = vid.read()
        frame = cv2.flip(frame,1)
        kernel = np.ones((3,3),np.uint8)

        # Ekran açıldığında belli bir kısmını işaretleyeceğimiz alanı ekleyelim
        roi = frame[100:300, 100:300]
        cv2.rectangle(frame,(100,100),(300,300),(211,234,21),1) # sol üst(100,100) ve sağ alt(300,300) noktalar

        # belli bir alandaki bir rengi o bölgedeki alandan ayırmak için o bölgenin renk modunu BGR dan HSV ye çevirmeliyiz
        # roi kısmını hsv moduna çevireceğiz
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # elimizin renk aralığını belirleyelim alt ve üst değerler
        lower_skin = np.array([0,20,70], np.uint8)
        upper_skin = np.array([20,255,255], np.uint8)

        # Roi içerisindeki elimi kalan alandan ayırmak istiyorum
        mask = cv2.inRange(hsv,lower_skin, upper_skin)
        # oluşacak karanlık noktaları beyazla dolduralım
        mask = cv2.dilate(mask, kernel, iteration = 4) # belirlediğimiz kernel siyah noktaları beyazlaştıracak
        mask = cv2.GaussianBlur(mask, (5,5), 100) # resimde var olan gürültüyü silmek için Gaussian blur kullandık

        #sınır çizgilerini bulalım
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # contour ların max değerlerini bulalım
        cnt = max(contours, key= lambda x: cv2.contourArea(x))

        epsilon = 0.0005*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)

        hull = cv2.convexHull(cnt)

        areaHull = cv2.contourArea(hull) # örtünün alanı
        areaCnt = cv2.contourArea(cnt) # elimin alanı
        areaRatio = ((areaHull - areaCnt)/areaCnt)*100 # elimizin olmadığı alan oranını bulmak için

        # dışbükey kusurlarını tespit edelim, (ele bağlı oluşan kusurlar)
        hull = cv2.convexHull(approx, returnPoints=False) # False:indisler, True:contour ları dönüyor
        defects = cv2.convexityDefects(approx, hull)

        k=0 # başta kusur sayısı

        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])

            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

            s = (a+b+c) / 2 # bu işlemi üçgenin alanını bulmak için kullanacagız
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            d = (2*area) / a #noktalar ve dış bükeyler arasındaki mesafeyi buluyoruz

            angle = math.acos((b**2+c**2-a**2)/(2*b*c))*57
            # benim açı değerim 90 dereceye eşit veya küçükse ve d mesafem de 30 dan büyükse burada bir kusur vardır diyeceğiz ve kusur sayımızı 1 arttıracağız

            if angle <=90 and d>30:
                k+=1
                cv2.circle(roi, far, 3, [24,221,42], -1)

            cv2.line(roi, start, end, [24,221,42], 2)

        k+=1
        font = cv2.FONT_HERSHEY_SIMPLEX

        if k==1:
            if areaCnt < 2000:
                cv2.putText(frame, "Put your hand in the box:", (0,50), font, (0,0,255), 0.5, cv2.LINE_AA)
            else:
                if areaRatio < 12:
                    cv2.putText(frame, "0", (0, 50), font, (0, 0, 255), 3, cv2.LINE_AA)
                elif areaRatio < 17.5:
                    cv2.putText(frame, "Best Luck", (0, 50), font, (0, 0, 255), 3, cv2.LINE_AA)
                else:
                    cv2.putText(frame, "1", (0, 50), font, (0, 0, 255), 3, cv2.LINE_AA)

        elif k==2:
            cv2.putText(frame, "2", (0, 50), font, (0, 0, 255), 3, cv2.LINE_AA)

        elif k==3:
            if areaRatio<27:
                cv2.putText(frame, "3", (0, 50), font, (0, 0, 255), 3, cv2.LINE_AA)
            else:
                cv2.putText(frame, "Ok", (0, 50), font, (0, 0, 255), 3, cv2.LINE_AA)

        elif k==4:
            cv2.putText(frame, "4", (0, 50), font, (0, 0, 255), 3, cv2.LINE_AA)

        elif k==5:
            cv2.putText(frame, "5", (0, 50), font, (0, 0, 255), 3, cv2.LINE_AA)

        else:
            cv2.putText(frame, "reposition", (10, 50), font, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow("mask", mask)
        cv2.imshow("frame", frame)

    except:
        pass

    g = cv2.waitKey(5) & 0xFF
    if g == 27:
        break

vid.release()
cv2.destroyAllWindows()

