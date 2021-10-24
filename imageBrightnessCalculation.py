import cv2
import numpy as np

# Numerator = Pay
# Denominator = Payda

imgGray = cv2.imread("resources/view1.jpg", 0)

numerator = np.sum(imgGray)
denominator = imgGray.shape[0] * imgGray.shape[1]

# sum2 = 0
# for i in range(0, imgGray.shape[0]):
#     for j in range(0, imgGray.shape[1]):
#         sum2 = imgGray[i][j] + sum2
# print(sum2)

brightness = numerator / denominator

print(brightness)

cv2.imshow("ImageGray", imgGray)
cv2.waitKey()
