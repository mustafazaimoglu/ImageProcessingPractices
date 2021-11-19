import math
import cv2
import numpy as np


def blur(img, size):
    temp_image = img.copy()
    w, h = temp_image.shape[0], temp_image.shape[1]
    result = np.empty((w, h), dtype="uint8")

    # ADDING NEW ROW AND COLUMN
    new_row = np.zeros((math.floor(size / 2), h), dtype="uint8")
    new_column = np.zeros((w + (math.floor(size / 2) * 2), math.floor(size / 2)), dtype="uint8")

    temp_image = np.insert(temp_image, w, new_row, axis=0)  # yeni satır ekleme w konumuna
    temp_image = np.insert(temp_image, 0, new_row, axis=0)  # yeni satır ekleme 0 konumuna
    temp_image = np.append(temp_image, new_column, axis=1)  # yeni sutun ekleme en sona
    temp_image = np.append(new_column, temp_image, axis=1)  # yeni sutun ekleme en basa

    w, h = temp_image.shape[0], temp_image.shape[1]

    for i in range((w - size) + 1):
        for j in range((h - size) + 1):
            arr = []
            for k in range(size):
                for t in range(size):
                    arr.append(temp_image[i + k, j + t])

            arr.sort()
            median_index = math.floor((size ** 2) / 2)
            result[i, j] = arr[median_index]

    return result


img_gray = cv2.imread("../resources/salt_pepper_2.png", 0)
img_median_blurred = blur(img_gray, 3)

cv2.imshow("Original", img_gray)
cv2.imshow("Median Blurred", img_median_blurred)
cv2.waitKey()
