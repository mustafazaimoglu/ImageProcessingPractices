import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../resources/independentObject3.png", 0)
w, h = img.shape

_, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
binary_image = np.zeros((w, h), dtype="uint8")

for i in range(0, w):
    for j in range(0, h):
        if threshold[i, j] == 255:
            binary_image[i, j] = 1

n = 1
result = binary_image.copy()
dict = {}

for i in range(1, w):
    for j in range(1, h):
        left = result[i, j - 1]
        center = binary_image[i, j]
        up = result[i - 1, j]

        if center != 0:
            if up == 0 and left == 0:
                result[i, j] = n
                n = n + 1
            elif up == 0:
                result[i, j] = left
            elif left == 0:
                result[i, j] = up
            else:
                if left > up:
                    result[i, j] = up
                    dict[left] = up
                else:
                    result[i, j] = left
                    dict[up] = left

product = result.copy()
len_dict = len(dict)

while len_dict > 0: # denklik tablosuna bakarak duzenleme
    len_dict = len_dict - 1
    for i in range(0, w):
        for j in range(0, h):
            if product[i, j] != 0:
                product[i, j] = dict[product[i, j]]

product_dict = {}
temp = 1

for i in range(0, w): # yeniden sıralama
    for j in range(0, h):
        if product[i, j] != 0:
            if not product[i, j] in product_dict:
                product_dict[product[i, j]] = temp
                temp = temp + 1

for i in range(0, w):
    for j in range(0, h):
        if product[i, j] != 0:
            product[i, j] = product_dict[product[i, j]]

plt.imshow(product, cmap='nipy_spectral')
plt.axis('off')
plt.tight_layout()
plt.show()
