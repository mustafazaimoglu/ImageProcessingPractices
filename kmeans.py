import cv2
import numpy as np

img = cv2.imread("resources/flower.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

twoDimage = img.reshape((-1, 3))
twoDimage = np.float32(twoDimage)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
attemps = 10
ret, label, center = cv2.kmeans(twoDimage, K, None, criteria, attemps, cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))
cv2.imshow("original", img)
cv2.imshow("K", result_image)
cv2.waitKey()
