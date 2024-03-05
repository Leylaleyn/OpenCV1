import cv2
import numpy as np
from matplotlib import pyplot as plt


"""img = np.zeros((500,500), np.uint8)
cv2.rectangle(img, (0,60), (200,150),(255,255,255),-1)"""

img = cv2.imread("helikopter.jpg")
b,g,r = cv2.split(img)


cv2.imshow("img", img)

plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.show()  #tek bir histogram üzerine bgr değerlerini çizdi

plt.hist(img.ravel(), 256, [0,256])
plt.show()






cv2.waitKey(0)
cv2.destroyAllWindows()















