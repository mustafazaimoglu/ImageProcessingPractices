import math
import cv2
import numpy as np


def blur(img, size, filter_ratio):
    w, h = img.shape[0], img.shape[1]
    result_image = np.empty((w, h), dtype="uint8")

    # ADDING NEW ROW AND COLUMN
    new_row = np.zeros((math.floor(size / 2), h), dtype="uint8")
    new_column = np.zeros((w + (math.floor(size / 2) * 2), math.floor(size / 2)), dtype="uint8")
    img = np.insert(img, w, new_row, axis=0)  # yeni satır ekleme w konumuna
    img = np.insert(img, 0, new_row, axis=0)  # yeni satır ekleme 0 konumuna
    img = np.append(img, new_column, axis=1)  # yeni sutun ekleme en sona
    img = np.append(new_column, img, axis=1)  # yeni sutun ekleme en basa

    w, h = img.shape[0], img.shape[1]

    for i in range((w - size) + 1):
        for j in range((h - size) + 1):
            temp_sum = 0
            for k in range(size):
                for t in range(size):
                    temp_sum += img[i + k][j + t]

            result = temp_sum / filter_ratio
            if result >= 255:
                result = 255
            result_image[i, j] = result

    return result_image


img_gray = cv2.imread("../resources/emma.jpg", 0)

img_gray_blurred = blur(img_gray, 3, 9)

cv2.imshow("Original Gray", img_gray)
cv2.imshow("Blurred Image", img_gray_blurred)
cv2.waitKey()
