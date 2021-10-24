import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("resources/flower.jpg", 0)

cv2.imshow("Org Gray", img)

CM = ((np.max(img) - np.min(img)) / (np.max(img) + np.min(img)))
newImage = CM * img

plt.imshow(newImage, cmap="gray")
plt.show()
cv2.waitKey()
