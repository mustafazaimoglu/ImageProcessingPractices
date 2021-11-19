import cv2
import numpy as np

img = cv2.imread("../resources/xray.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_threshold = img_gray.copy()

threshold_value = 220
w, h = img_gray.shape[0], img_gray.shape[1]

for i in range(w):
    for j in range(h):
        if img_threshold[i, j] > 30:
            img_threshold[i, j] = 255
        else:
            img_threshold[i, j] = 0

cv2.imshow("Original", img)
cv2.imshow("Gray", img_gray)
cv2.imshow("Binary Threshold", img_threshold)
cv2.waitKey()
