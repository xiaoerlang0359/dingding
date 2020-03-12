import cv2
import numpy as np

src = cv2.imread("E:\\assignment\\1\\1.jpg")

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
low_hsv = np.array([178, 43, 46])
high_hsv = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
ret, binary = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(binary, kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if len(contours) > 0:
    counter = 0
    boxes = [cv2.boundingRect(c) for c in contours]
    for box in boxes:
        x, y, w, h = box
        if (w > 20) & (h > 15):
            cv2.rectangle(src, (x, y), (x + w, y + h), (153, 153, 0), 2)
            counter = counter + 1
    print(counter)
    cv2.imshow('image', src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
