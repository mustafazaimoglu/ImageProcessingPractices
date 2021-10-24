import cv2

img = cv2.imread("resources/emma.jpg")

gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)  # zero means border type

median_blur = cv2.medianBlur(img, 7)
#  verilen aralıkta küçük bir matrix alarak değerlerini sort ettikten sonra medyan değeri merkeze yazılır.

cv2.imshow("Original", img)
cv2.imshow("Gaussian Result", gaussian_blur)
cv2.imshow("Median Result", median_blur)
cv2.waitKey()
