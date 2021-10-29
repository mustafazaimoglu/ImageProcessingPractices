import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../resources/emma.jpg")
img = cv2.resize(img, (512, 320))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray_hist = cv2.calcHist([img_gray], [0], None, [255], [0, 255])
equalized_img = cv2.equalizeHist(img_gray)
equalized_hist = cv2.calcHist([equalized_img], [0], None, [255], [0, 255])

CM = ((np.max(img_gray) - np.min(img_gray)) / (np.max(img_gray) + np.min(img_gray)))
michalson = CM * img_gray

_, binary_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
gaussian_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)

kernel = np.ones((3, 3), dtype="uint8")
eroded = cv2.erode(binary_thresh, kernel, iterations=1)
dilate = cv2.dilate(binary_thresh, kernel, iterations=1)
gradient = dilate - eroded

opening = cv2.morphologyEx(binary_thresh, cv2.MORPH_OPEN, kernel)  # erode,dilate,gradient,opening,closing

laplace = cv2.Laplacian(eroded, cv2.CV_32F)

gauss_noise = np.random.normal(0, 1, img_gray.size)
gauss_noise = gauss_noise.reshape(img_gray.shape[0], img_gray.shape[1]).astype('uint8')

gauss_image = cv2.add(img_gray,gauss_noise)

mean_filter_kernel = np.ones((3, 3), dtype="uint8") / 9.0

mean = cv2.filter2D(img_gray, -1, mean_filter_kernel)  # kernel oluşturulduktan sonra her filtre için çalışır
median = cv2.medianBlur(img_gray, 3)
gauss = cv2.GaussianBlur(img_gray, (3, 3), 0)
bilateral = cv2.bilateralFilter(img_gray, 3, 70, 50)

inverted = np.invert(img_gray)

# plt.figure()
# plt.plot(img_gray_hist)
# plt.figure()
# plt.plot(equalized_hist)
# plt.show()
# plt.imshow(michalson, cmap="gray")
# plt.show()

cv2.imshow("Original", img)
cv2.imshow("Gray", img_gray)
cv2.imshow("Binary Thresh", binary_thresh)
cv2.imshow("Gauss Thresh", gaussian_thresh)
cv2.imshow("Erode", eroded)
cv2.imshow("Dilate", dilate)
cv2.imshow("Gradient", gradient)
cv2.imshow("Opening", opening)
cv2.imshow("Laplace", laplace)
cv2.imshow("Gauss Noisy", gauss_image)
cv2.imshow("Mean", mean)
cv2.imshow("Median", median)
cv2.imshow("Gauss", gauss)
cv2.imshow("Bilateral", bilateral)
cv2.imshow("Inverted", inverted)
cv2.waitKey()
