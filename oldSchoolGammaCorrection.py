import cv2
import numpy as np

img = cv2.imread("resources/emma.jpg")

w, h, d = img.shape[0], img.shape[1], img.shape[2]
imgGammaCorrected025 = np.zeros(shape=(w, h, d))
imgGammaCorrected138 = np.zeros(shape=(w, h, d))
imgGammaCorrected225 = np.zeros(shape=(w, h, d))

c = 1
for i in range(w):
    for j in range(h):
        for k in range(d):
            imgGammaCorrected025[i, j, k] = c * ((img[i, j, k] / 255) ** 0.25)
            imgGammaCorrected138[i, j, k] = c * ((img[i, j, k] / 255) ** 1.38)
            imgGammaCorrected225[i, j, k] = c * ((img[i, j, k] / 255) ** 2.25)

cv2.imshow("Org", img)
cv2.imshow("0.25", imgGammaCorrected025)
cv2.imshow("1.38", imgGammaCorrected138)
cv2.imshow("2.25", imgGammaCorrected225)

cv2.waitKey()
