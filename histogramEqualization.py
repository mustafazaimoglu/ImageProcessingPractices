import cv2
import numpy as np
import matplotlib.pyplot as plt

img_gray = cv2.imread("resources/flower.jpg",0)

equ = cv2.equalizeHist(img_gray)

res = np.hstack((img_gray, equ))
cv2.imshow("stacked", res)

original_hist = cv2.calcHist([img_gray], [0], None, [255], [0, 255])
outcome_hist = cv2.calcHist([equ], [0], None, [255], [0, 255])

plt.figure(1)
plt.plot(original_hist)
plt.figure(2)
plt.plot(outcome_hist)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
