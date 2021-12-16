import cv2
import numpy as np
from skimage.util import random_noise

img = cv2.imread("../resources/kids.jpg")

noisy_img = random_noise(img, mode="s&p", amount=0.05)  # adding noises
noisy_img = np.array(255 * noisy_img, dtype="uint8")

noisy_gray = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2GRAY)

median_gray = cv2.medianBlur(noisy_gray, 3)  # temizlemek için

# Median --> Mean (Kırışık yerleri düzeltmek için)
kernel = np.ones((5, 5)) / 25.0  # mean filter
smooth_gray = cv2.filter2D(median_gray, -1, kernel)

gamma_corrected = np.array(255 * (smooth_gray / 255) ** 3.25,
                           dtype="uint8")  # gölgelenderen kaynaklanan sıkıntıları gidermek

face_cascade = cv2.CascadeClassifier("../data/haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gamma_corrected)

print("Tespit edilen yüz sayısı :", f"{len(faces)}")

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), color=(255, 0, 200), thickness=2)

# cv2.imshow("Noisy", noisy_img)
# cv2.imshow("Noisy_Gray", noisy_gray)
# cv2.imshow("Cleaned_Gray", median_gray)
# cv2.imshow("Median -> Mean", smooth_gray)
# cv2.imshow("Gamma Corrected", gamma_corrected)
cv2.imshow("Result", img)
cv2.waitKey()

# median --> gaussian (for an extra more cleaning)
# smooth_gray = cv2.GaussianBlur(median_gray, (5, 5), 0)  # yumuşatma yapmak için

# kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])  # keskinleştirme
# noisy_gray = cv2.filter2D(noisy_gray, -1, kernel)
