import cv2
import numpy as np
import math


def prewitt_edge_detect(img, x_kernel, y_kernel):
    temp_image = img.copy()
    w, h = temp_image.shape
    size = len(x_kernel)

    # ADDING NEW ROW AND COLUMN
    new_row = np.zeros((math.floor(size / 2), h), dtype="uint8")
    new_column = np.zeros((w + (math.floor(size / 2) * 2), math.floor(size / 2)), dtype="uint8")

    temp_image = np.insert(temp_image, w, new_row, axis=0)
    temp_image = np.insert(temp_image, 0, new_row, axis=0)
    temp_image = np.append(temp_image, new_column, axis=1)
    temp_image = np.append(new_column, temp_image, axis=1)

    w, h = temp_image.shape

    temp_image_result = np.empty((w, h), dtype="uint8")
    temp_image_y = temp_image.copy()

    for i in range((w - size) + 1):
        for j in range((h - size) + 1):
            x_negatives, y_negatives, x_positives, y_positives = 0, 0, 0, 0
            for k in range(size):
                for t in range(size):
                    if x_kernel[k, t] == -1:
                        x_negatives += temp_image[i + k, j + t] * -1
                    elif x_kernel[k, t] == 1:
                        x_positives += temp_image[i + k, j + t]

                    if y_kernel[k, t] == -1:
                        y_negatives += temp_image[i + k, j + t] * -1
                    elif y_kernel[k, t] == 1:
                        y_positives += temp_image[i + k, j + t]

            result_x = x_positives + x_negatives
            result_y = y_positives + y_negatives

            if result_x > 255:
                result_x = 255
            elif result_x < 0:
                result_x = 0

            if result_y > 255:
                result_y = 255
            elif result_y < 0:
                result_y = 0

            if result_x > result_y:
                temp_image_result[i, j] = result_x
            else:
                temp_image_result[i, j] = result_y

    return temp_image_result


img_gray = cv2.imread("resources/shapes_black.jpg", 0)
x_filter = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
y_filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewitt_edge_detected = prewitt_edge_detect(img_gray, x_filter, y_filter)
cv2.imshow("Original", img_gray)
cv2.imshow("temp", img_prewitt_edge_detected)
cv2.waitKey()
