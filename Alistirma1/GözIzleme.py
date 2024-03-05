# Dikkat göz bebeği herkeste siyahtır (ortak özellik)
# göz çevresine önce roi çizeceğiz
# daha sonra göz bebeğinin oraya bir rectangle çizdireceğiz

import cv2

vid = cv2.VideoCapture("eye_motion.mp4")

while 1:
    ret, frame = vid.read()

    if ret is False:
        break

    roi = frame[80:210, 230:450]
    rows,cols,_ = roi.shape # satır , sütunları aldık

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # kontur olarak bınary_ınv kullanacağız çünkü siyah göz bebeğini beyaz yapıp geri kalan çevreyi siyah yapacağız
    _, threshold = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY_INV)

# göz bebeğinin konturlerini bulalım
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse = True) # kontur değerlerimi bu fonksiyona göre sırala dedik, reverse = Tersten sıralaması için

   # en büyük alana sahip olan kontur'e dikdörtgen çizeceğiz, yukarıda da en büyükten küçüğe doğru sıraladık
    for cnt in contours:
        
        (x,y,w,h) = cv2.boundingRect(cnt) #bu koordinat değerlerini boundingRect ile çekebiliyoruz
        cv2.rectangle(roi, (x,y), (x+w, y+h), (255,255,0), 2)  # sol üst koordinatım (x,y) (x+w=genişlik, y+h=yükseklik)
        cv2.line(roi,(x + int(w/2),0), (x +int(w/2),rows), (0,255,255),2)
        cv2.line(roi,(0,y + int(h/2)), (cols,y + int(h/2)), (0,255,255),2)

        break

    frame[80:210, 230:450] = roi
    cv2.imshow("frame", frame)

    #cv2.imshow("roi", roi)
    # cv2.imshow("t_roi", threshold)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()