import cv2
import matplotlib.pyplot as plt

img = cv2.imread("resources/flower.jpg", 0)
img = cv2.medianBlur(img, 5) # histogramdak gereksiz yükselmeleri törpüler.
ret, th1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

titles = ["Original Image", "Global Thresholding (v = 150)", "Adaptif Ortalama Esikleme", "Adaptif Gaussian Esikleme"]

images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], "gray")
    plt.xticks([])
    plt.yticks([])

plt.show()
