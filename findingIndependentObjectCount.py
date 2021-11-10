import cv2
from skimage import measure
from skimage import filters
import matplotlib.pyplot as plt
import numpy as np

n = 12
l = 256

np.random.seed(1) # random da aynı sonuç çıkması için
im = np.zeros((l, l))
points = l * np.random.random((2, n ** 2)) # [2,144] bir dizi oluşturur random sayılardan ve 256 ile çarpar

im[(points[0]).astype(int), (points[1]).astype(int)] = 1 # denk gelen koordinatlara 1 girer
im = filters.gaussian(im, sigma= l / (4. * n)) # yumşatma yaparak 1 i etrafa yayar yuvarlak oluşturur

blobs = im > 0.7 * im.mean() # matrisi True False matrisine dönüştürür.

all_labels = measure.label(blobs) # True-False matrislerini numaralandırarak sayar
blobs_labels = measure.label(blobs, background=0)

print(np.max(blobs_labels)) # object Count

plt.figure(figsize=(9,3.5))
plt.subplot(131)
plt.imshow(blobs, cmap='gray')
plt.axis('off')
plt.subplot(132)
plt.imshow(all_labels, cmap='nipy_spectral')
plt.axis('off')
plt.subplot(133)
plt.imshow(blobs_labels, cmap='nipy_spectral')
plt.axis('off')
plt.tight_layout()
plt.show()