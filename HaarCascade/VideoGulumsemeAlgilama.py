import cv2

vid = cv2.VideoCapture("smile.mp4")

smile_cascade = cv2.CascadeClassifier('smile.xml')
face_cascade = cv2.CascadeClassifier('frontalface.xml')

while 1:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (640,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.4, 4)

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[x:x + w, y:y + h]
        roi_img = frame[x:x + w, y:y + h]

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.3, 4)
        for (ex, ey, ew, eh) in smiles:
            cv2.rectangle(roi_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('videos', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
