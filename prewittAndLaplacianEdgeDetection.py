import cv2
import numpy as np

img = cv2.imread("resources/shapes.jpg", 0)

# prewitt edge detection
x_filter = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
y_filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

image_x = cv2.filter2D(img, -1, x_filter)
image_y = cv2.filter2D(img, -1, y_filter)

laplace1 = cv2.Laplacian(img, cv2.CV_16S, ksize=5)  # 2.türev tabanlı çalışır
laplace2 = cv2.Laplacian(img, cv2.CV_32F)
laplace3 = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow("Org", img)
cv2.imshow("Yatay", image_x)
cv2.imshow("Dikey", image_y)
cv2.imshow("Laplace16S", laplace1)
cv2.imshow("Laplace32F", laplace2)
cv2.imshow("Laplace64F", laplace3)
cv2.waitKey()
