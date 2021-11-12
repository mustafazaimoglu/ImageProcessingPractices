import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('resources/shapes.jpg',0)

# çıkış veri tipi = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
# çıkış veri tipi = cv2.CV_64F. sonra onun mutlak değeri alınır ve cv2.CV_8U e dönüştürülür
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Orijinal'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()