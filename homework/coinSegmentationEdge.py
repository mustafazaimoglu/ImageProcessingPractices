import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage import measure

coins = data.coins()
coins_copy = coins.copy()

gamma_corrected = np.array(255 * (coins_copy / 255) ** 1.68, dtype="uint8")

median_filtered = cv2.medianBlur(gamma_corrected, 11)

plt.figure("Original")
plt.imshow(coins_copy, cmap="gray")
plt.figure("Gamma Corrected")
plt.imshow(gamma_corrected, cmap="gray")
plt.figure("Median Filtered")
plt.imshow(median_filtered, cmap="gray")

kernel_laplace = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
laplace = cv2.filter2D(median_filtered, -1, kernel_laplace)

plt.figure("Laplace Filter")
plt.imshow(laplace, cmap="gray")

_, thresh = cv2.threshold(laplace, 16, 255, cv2.THRESH_BINARY)

plt.figure("Manual Threshold")
plt.imshow(thresh, cmap="gray")

filled_contour = np.zeros_like(coins)
contour, _ = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# FILL THE CONTOURS
for cnt in contour:
    cv2.drawContours(filled_contour, [cnt], 0, 255, cv2.FILLED)

plt.figure("Filled Contour")
plt.imshow(filled_contour, cmap="gray")

kernel_ellipse_3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
filled_contour = cv2.morphologyEx(filled_contour, cv2.MORPH_OPEN, kernel_ellipse_3, iterations=2)

plt.figure("Morph Open")
plt.imshow(filled_contour, cmap="gray")

separated = filled_contour & gamma_corrected

plt.figure("And Operation")
plt.imshow(separated, cmap="gray")

separated_boolean_matrix = separated > 0  # Boolean Matrix

all_labels = measure.label(separated_boolean_matrix)

plt.figure("Colorful Virsualization")
plt.imshow(all_labels, cmap='nipy_spectral')

plt.show()
cv2.waitKey()
