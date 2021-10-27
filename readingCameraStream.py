import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()

    if success:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary_thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

        kernel = np.ones((5, 5), dtype="uint8")
        erode = cv2.erode(binary_thresh, kernel, iterations=1)

        cv2.imshow("Video Output", frame)
        cv2.imshow("Video Output Gray", gray)
        cv2.imshow("Video Output1", binary_thresh)
        cv2.imshow("Erode", erode)

        if cv2.waitKey(10) & 0xFF == ord('q'):  # with this we can close the window by pressing 'q'
            break
    else:
        print("Reading Error")
        break
