import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("resources/image1.jpg")  # ,0 means gray scale
cv2.imshow("Original", img)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", imgGray)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]
# cv2.imshow("Blue", B)
# cv2.imshow("Green", G)
# cv2.imshow("Red", R)

imgShape = img.shape
RShape = R.shape

print(imgShape)
print(RShape)

x = 2
y = 2
channel = 2

densityOfImg = img[y, x, channel]
densityOfR = R[y, x]

print(densityOfImg)
print(densityOfR)

histImgB = cv2.calcHist([img], [0], None, [256],
                        [0, 256])  # to get histogram of image (src,layer,mask,last 2 is constant)
histImgG = cv2.calcHist([img], [1], None, [256], [0, 256])
histImgR = cv2.calcHist([img], [2], None, [256], [0, 256])
histB = cv2.calcHist([B], [0], None, [256], [0, 256])
histImgGray = cv2.calcHist([imgGray], [0], None, [256], [0, 256])

plt.figure(1)
plt.plot(histImgB)
plt.plot(histImgG)
plt.plot(histImgR)

plt.figure(2)
plt.plot(histImgGray)

plt.figure(3)
# plt.plot(histB)
plt.hist(imgGray.ravel(), 256,
         [0, 256])

plt.show()
cv2.waitKey(0)
