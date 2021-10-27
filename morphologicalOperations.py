import cv2
import numpy as np
from skimage.util import random_noise

img = cv2.imread("resources/test2.jpg", 0)

ret, thresh_image = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
noisy_img = random_noise(thresh_image, mode="s&p", amount=0.05)
noisy_img = np.array(255 * noisy_img, dtype="uint8")

kernel = np.ones((5, 5), dtype="uint8")

erode = cv2.erode(thresh_image, kernel, iterations=1)  # 0 yapmaya çalışılması and gate
dilate = cv2.dilate(thresh_image, kernel, iterations=1)  # 1 yapmaya çalışmak or gate

new_kernel1 = np.ones((3, 3), dtype="uint8")
new_kernel2 = np.ones((5, 5), dtype="uint8")

opening = cv2.morphologyEx(noisy_img, cv2.MORPH_OPEN, new_kernel1)  # erozyon uygulanan resme genişleme ugulanması
closing = cv2.morphologyEx(noisy_img, cv2.MORPH_CLOSE, new_kernel2)  # genişleme uygulanan resme erozyon uygulanması
gradient = cv2.morphologyEx(erode, cv2.MORPH_GRADIENT, new_kernel1)  # gradient = dilate - erode

cv2.imshow("Thresh", thresh_image)
cv2.imshow("Noisy", noisy_img)
cv2.imshow("Erozyon", erode)
cv2.imshow("Genisleme", dilate)
cv2.imshow("Acma", opening)
cv2.imshow("Kapatma", closing)
cv2.imshow("Gradyan", gradient)

cv2.waitKey()
