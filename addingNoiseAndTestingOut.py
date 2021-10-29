import cv2
import numpy as np
from skimage.util import random_noise

img = cv2.imread("resources/emma.jpg")
gauss = np.random.normal(0, 1, img.size)
gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
noise_img = random_noise(img, mode="s&p", amount=0.1)
noise_img = np.array(255 * noise_img, dtype="uint8")

img_gauss = cv2.add(img, gauss)
cv2.imshow("Gauss Noise", gauss)

gaussian_blur = cv2.GaussianBlur(noise_img, (5, 5), 0)
blur_filter = np.ones((3, 3), np.float64) / 9.0
average_filter = cv2.filter2D(noise_img, -1, blur_filter)
median_filter = cv2.medianBlur(noise_img, 5)
bilateral_filter = cv2.bilateralFilter(noise_img, 3, 70, 50)

cv2.imshow("Original", img)
cv2.imshow("Gauss gurultulu goruntu", img_gauss)
cv2.imshow("S&P Gurultu", noise_img)
cv2.imshow("Gauss iyilestirilmis goruntu", gaussian_blur)
cv2.imshow("Average filter iyilestirilmis goruntu", average_filter)
cv2.imshow("Median filter iyilestirilmis goruntu", median_filter)
cv2.imshow("Bilateral filter iyilestirilmis goruntu", bilateral_filter)
cv2.waitKey()
