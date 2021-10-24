import cv2

img = cv2.imread("resources/image1.jpg")

cv2.imshow("Output", img)
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # RGB to HSV
cv2.imshow("HSV", hsv_image)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)
cv2.waitKey(0)
