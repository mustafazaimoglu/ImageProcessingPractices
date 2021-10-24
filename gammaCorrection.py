import cv2
import numpy as np

img = cv2.imread("resources/flower.jpg")

for i, gamma in enumerate([0.1, 0.5, 1.2, 2.2]):
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype="uint8")
    cv2.imshow("Gamma Convertion " + str(gamma), gamma_corrected)

cv2.waitKey()
