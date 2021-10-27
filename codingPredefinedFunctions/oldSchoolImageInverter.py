import cv2
import matplotlib.pyplot as plt

imgGray = cv2.imread("../resources/lambo.jpg", 0)
w, h = imgGray.shape[0], imgGray.shape[1]

imgInverted = imgGray.copy()

biggest = 0
for i in range(w):
    for j in range(h):
        if biggest < imgGray[i, j]:
            biggest = imgGray[i, j]

print(biggest)

for i in range(w):
    for j in range(h):
        imgInverted[i, j] = biggest - imgInverted[i, j]

for i, img in enumerate([imgGray, imgInverted]):
    plt.subplot(1, 2, i + 1)
    plt.imshow(img, "gray")
    plt.xticks([])
    plt.yticks([])

plt.show()
