import cv2
import numpy as np

from skimage import data

coins = data.coins()
coins_copy = coins.copy()

gamma_three = np.array(255 * (coins_copy / 255) ** 3.30, dtype="uint8")

gamma_half = np.array(255 * (gamma_three / 255) ** 0.50, dtype="uint8")

gamma_half_org = np.array(255 * (coins_copy / 255) ** 1.67, dtype="uint8")

cv2.imshow("0",coins)
cv2.imshow("1",gamma_three)
cv2.imshow("2",gamma_half)
cv2.imshow("3",gamma_half_org)
cv2.waitKey()
