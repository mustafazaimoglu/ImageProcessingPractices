import cv2
import numpy as np

img = cv2.imread("resources/kids.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur_filter1 = np.ones((3, 3)) / 25.0
# img_gray = cv2.filter2D(img_gray, -1, blur_filter1)

face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
yuzler = face_cascade.detectMultiScale(img_gray,1.5)
# yuzler = face_cascade.detectMultiScale(img_gray)
print("Tespit edilen yüz sayısı :", f"{len(yuzler)}")

for x, y, w, h in yuzler:
    cv2.rectangle(img, (x, y), (x + w, y + h), color=(255, 0, 255), thickness=2)
    cv2.imshow("sonuc", img)

cv2.waitKey()
