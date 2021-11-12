import cv2
import numpy as np

img = cv2.imread("resources/flower.jpg", 0)
cv2.imshow("Original", img)

c = 1
logImage = c * np.log(1 + img)
logImage = np.array(logImage, dtype=np.uint8) # float gelen değerleri resim datatype olan uint8 e dönüştürüyor.
cv2.imshow("Logaritmik donusum", logImage)
logImage = 255 / (c * np.log(1 + img)) # görünürlülüğü arttırmak için
logImage = np.array(logImage, dtype=np.uint8)
cv2.imshow("Logaritmik donusum_255", logImage)

cv2.waitKey()
