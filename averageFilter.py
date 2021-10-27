import cv2
import numpy as np

img = cv2.imread("resources/emma.jpg", 0)

blur_filter1 = np.ones((3, 3)) / 9.0
blur_filter2 = np.ones((8, 8)) / 9.0
blur_filter3 = np.ones((12, 12)) / 9.0

img_blur1 = cv2.filter2D(img, -1, blur_filter1)
img_blur2 = cv2.filter2D(img, -1, blur_filter2)
img_blur3 = cv2.filter2D(img, -1, blur_filter3)

cv2.imshow("org", img)
cv2.imshow("blur1", img_blur1)
cv2.imshow("blur2", img_blur2)
cv2.imshow("blur3", img_blur3)
cv2.waitKey()
