import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import sobel
from skimage.measure import label
from skimage.segmentation import watershed, expand_labels
from skimage.color import label2rgb
from skimage import data

coins = data.coins()
coins_copy = coins.copy()

# TO MAKE IMAGE DARKER
gamma_three = np.array(255 * (coins_copy / 255) ** 3.30, dtype="uint8")

# TO MAKE IMAGE MORE BRIGHT
gamma_half = np.array(255 * (gamma_three / 255) ** 0.50, dtype="uint8")

median_filtered = cv2.medianBlur(gamma_half, 9)

plt.figure("Original")
plt.imshow(coins_copy, cmap="gray")
plt.figure("Median Filtered")
plt.imshow(median_filtered, cmap="gray")

thresh_value, thresh = cv2.threshold(median_filtered, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(thresh_value)

plt.figure("Normal Thresh (OTSU)")
plt.imshow(thresh, cmap="gray")

filled_contour = np.zeros_like(coins)
contour, hier = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# FILL THE CONTOURS
for cnt in contour:
    cv2.drawContours(filled_contour, [cnt], 0, 255, cv2.FILLED)

# DELETE BIGGEST OBJECT
cnt = max(contour, key=cv2.contourArea)
cv2.drawContours(filled_contour, [cnt], -1, 0, cv2.FILLED)

kernel_ellipse_3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

filled_contour = cv2.dilate(filled_contour, kernel_ellipse_3, iterations=1)

plt.figure("Contour Filled Thresh + Object Deleted + Dilated")
plt.imshow(filled_contour, cmap="gray")

separated = coins & filled_contour
plt.figure("And Operation")
plt.imshow(separated, cmap="gray")

edges = sobel(separated)

plt.figure("Sobel Edges")
plt.imshow(edges, cmap="gray")

markers = np.zeros_like(coins)
foreground, background = 1, 2
markers[separated < 30.0] = background
markers[separated > 50.0] = foreground

ws = watershed(edges, markers)
seg1 = label(ws == foreground)
expanded = expand_labels(seg1, distance=6)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(13, 5), sharex=True, sharey=True)
axes[0].imshow(coins)
axes[0].set_title('Orijinal')
color1 = label2rgb(seg1, image=coins, bg_label=0)
axes[1].imshow(color1)
axes[1].set_title('Sobel+Watershed')
color2 = label2rgb(expanded, image=coins, bg_label=0)
axes[2].imshow(color2)
axes[2].set_title('Genişletilen Etiketler')

for a in axes:
    a.axis('off')

fig.tight_layout()
plt.show()
cv2.waitKey()
