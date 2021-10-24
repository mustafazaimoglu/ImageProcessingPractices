import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("resources/flower.jpg", 0)
invertedImg = np.invert(img)

negativeImg = 255 - img  # negatif image 255 den cıkarmaktır, tersini almak en yogundan cıkarmak

img2 = cv2.imread("resources/emma.jpg", 0)

biggest = np.max(img2)

img2ManualInverted = biggest - img2
imageStack = [img2, img2ManualInverted]
imageStackTitles = ["Org", "Manual Inverted"]

for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(imageStack[i], "gray")
    plt.title(imageStackTitles[i])
    plt.xticks([])
    plt.yticks([])

imgStackHorizontal = np.hstack((img2, img2ManualInverted))
imgStackVertical = np.vstack((img2, img2ManualInverted))

cv2.imshow("Original", img)
cv2.imshow("inverted", invertedImg)
cv2.imshow("Negative", negativeImg)
cv2.imshow("Horizontal", imgStackHorizontal)
cv2.imshow("Vertical", imgStackVertical)
plt.show()
cv2.waitKey(0)
