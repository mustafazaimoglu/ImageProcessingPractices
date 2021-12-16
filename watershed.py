import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.filters import sobel
from skimage.measure import label
from skimage.segmentation import watershed, expand_labels
from skimage.color import label2rgb
from skimage import data, exposure

coins = data.coins()

# kenar bulma ve watershed ile bölütleme.
plt.figure("org")
plt.imshow(coins,cmap="gray")

edges = sobel(coins)
plt.figure()
plt.imshow(edges,cmap="gray")

# cv2.imshow("sobel", edges)
# bazı arka plan ve ön plan piksellerini yoğunluk değerlerine bakarak etiketleme.
# bu etiketleme watershed algoritması için temel teşkil edecek.
markers = np.zeros_like(coins)
foreground, background = 1, 2
markers[coins < 30.0] = background
markers[coins > 150.0] = foreground

# cv2.imshow("esikleme", markers * 200)
ws = watershed(edges, markers)
seg = label(ws == foreground)
expanded = expand_labels(seg, distance=6)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(13, 5), sharex=True, sharey=True)
axes[0].imshow(coins)
axes[0].set_title('Orijinal')
color1 = label2rgb(seg, image=coins, bg_label=0)
axes[1].imshow(color1)
axes[1].set_title('Sobel+Watershed')
color2 = label2rgb(expanded, image=coins, bg_label=0)
axes[2].imshow(color2)
axes[2].set_title('Genişletilen etiketler')

for a in axes:
    a.axis('off')

fig.tight_layout()
plt.show()
