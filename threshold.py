import cv2
import matplotlib.pyplot as plt

img = cv2.imread("resources/flower.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# hist = cv2.calcHist([imgGray],[0],None,[256],[0,256])
#
# plt.figure(0)
# plt.plot(hist)
# plt.show()
                            # source , eşik, verilecek değer(yerine yazılacak değer)
ret, thresh1 = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY)  # eşik değer altı 0 a üstü 255 e eşitlenir
ret, thresh2 = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY_INV)  # eşik değer altı 255 e ustu 0 a eşitlenir
ret, thresh3 = cv2.threshold(imgGray, 120, 255, cv2.THRESH_TRUNC)  # esik değer ve üstü eşik değere esitlenir, altı ise aynı kalır
ret, thresh4 = cv2.threshold(imgGray, 120, 255, cv2.THRESH_TOZERO)  # esik değer altı 0 a eşitlenir, üstü aynı kalır
ret, thresh5 = cv2.threshold(imgGray, 120, 255, cv2.THRESH_TOZERO_INV)  # eşik değer üstü 0 eşitlenir, altı aynen kalır

cv2.imshow("Binary Threshold", thresh1)
cv2.imshow("Binary Threshold Inverted", thresh2)
cv2.imshow("Truncated Threshold", thresh3)
cv2.imshow("Set to 0", thresh4)
cv2.imshow("Set to 0 Inverted", thresh5)

myResult = cv2.inRange(imgGray, 100, 175)  # verilen aralık 100-175 255 yapılır kalanlar 0 eşitlenir.
cv2.imshow("Aralikli Esitleme", myResult)

cv2.waitKey()
