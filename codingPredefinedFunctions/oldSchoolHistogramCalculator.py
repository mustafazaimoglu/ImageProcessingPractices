import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../resources/image1.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", imgGray)

hist = np.zeros(256)
w = img.shape[0]
h = img.shape[1]

for i in range(0, w):
    for j in range(0, h):
        instantValue = imgGray[i, j]
        hist[instantValue] = hist[instantValue] + 1

functionResultHistogram = cv2.calcHist([imgGray], [0], None, [256], [0, 256])

plt.figure("Old School Histogram")
plt.plot(hist)
print(np.sum(hist))

plt.figure("OpenCV Function Histogram")
plt.plot(functionResultHistogram)
print(np.sum(functionResultHistogram))

plt.show()
cv2.waitKey()
