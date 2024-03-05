import cv2
import numpy as np

img = cv2.imread("opencv.png")
cv2.imshow("OpenCV",img)

print(img.shape)   # width, height, channel
#boyutları 249, 282
# channel : 3 -> renkli
# channel : 1 -> grayscale

# Shape
print("height: {} pixels".format(img.shape[0]))
print("width: {} pixels".format(img.shape[1]))
print("channel: {} pixels".format(img.shape[2])) # resmimiz renkli değilse sonuç alamayız hata verir

# Size
print("Image Size: {}".format(img.size))  # Size : Width x height x channel (249*202*3)

# Veri Tipi
print("Data Type: {}".format(img.dtype))



cv2.waitKey(0)
cv2.destroyAllWindows()















