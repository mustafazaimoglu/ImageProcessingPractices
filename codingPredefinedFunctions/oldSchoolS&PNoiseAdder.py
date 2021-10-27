import math
import random

import cv2


def add_noise(img):
    w, h = img.shape
    pixel_size = img.size
    min = math.floor(pixel_size / 30)
    max = math.floor(pixel_size / 20)

    salt_size = random.randint(min, max)
    for i in range(salt_size):
        y_coordinate = random.randint(0, w - 1)
        x_coordinate = random.randint(0, h - 1)
        img[y_coordinate, x_coordinate] = 255

    pepper_size = random.randint(min, max)
    for i in range(pepper_size):
        y_coordinate = random.randint(0, w - 1)
        x_coordinate = random.randint(0, h - 1)
        img[y_coordinate, x_coordinate] = 0

    return img


img_gray = cv2.imread("../resources/emma.jpg", 0)
cv2.imshow("Original", img_gray)
img_noised = add_noise(img_gray)
cv2.imshow("Noised", img_noised)
cv2.imshow("Median Filtered", cv2.medianBlur(img_noised, 3))
cv2.waitKey()
