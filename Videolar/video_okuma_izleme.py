import cv2

# webcam üzerinden görüntüleri alacağız
# cap = cv2.VideoCapture(0)  #webcam'den okuyacaksak 0 değerini gireriz, bilgisayara bağlı başka bir kamerayı kullanacaksak 1,2 gibi değerler girebiliriz

# video dosyasından görüntüyü alma
cap = cv2.VideoCapture("antalya.mp4")

#
while True:    # Videoların karelerini tek tek okuyarak gösterebilmek için döngü açmak zorundayız

    ret, frame = cap.read()  # cap.read() 2 değer döndürür, ilki videoları doğru okuduysa True yanlış ise False, ikincisi' de frameler yani karelerdir
    if ret == 0:  # video bitmiştir video bitince döngüden çıksın videp kapansın
        break
    frame = cv2.flip(frame, 1) # aldığımız görüntüyü istediğimiz her eksene göre yansıtır  1-> y eksenine göre tersini alıyor
    cv2.imshow("Antalya", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):  # her frame 30 sn gösterilecek
        break  # q tuşuna basınca ekranı kapatır



cap.release()
"""VideoCapture nesnesinin kaynakla (genellikle bir video dosyası 
veya kamera akışı) ilişkisini sonlandırmak için kullanılır.
Bu yöntemi kullanarak kaynağa olan bağlantıyı serbest bırakabilir ve 
kaynak dosyanın veya kamera akışının kullanımını tamamladığınızda kaynağı
serbest bırakarak kaynaklarınızı etkili bir şekilde yönetebilirsiniz"""

cv2.destroyAllWindows()






