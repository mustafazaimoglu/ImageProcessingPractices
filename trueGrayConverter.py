import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("resources/image1.jpg")  # ,0 means gray scale
cv2.imshow("Original", img)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)

img2 = cv2.imread("resources/image1.jpg", 0)  # reading with gray color
cv2.imshow("Original2", img2)

imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B  # to convert standard gray color
plt.imshow(imgGray, cmap="gray")
plt.show()

cv2.waitKey(0)
