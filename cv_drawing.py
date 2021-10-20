import cv2
import numpy as np

img = np.zeros((400, 600, 3), np.uint8)
# img[:] = 255, 255, 255
# img[200:300, 100:200] = 255, 255, 255

cv2.line(img, (0, 400), (600, 0),(255, 0, 0), 3)
cv2.line(img, (0, 200), (600, 200),(255, 0, 0), 3)
cv2.line(img, (0, 0), (600, 400),(255, 0, 0), 3)
cv2.rectangle(img, (300,200), (600,400), (0, 200, 0), 5)
cv2.rectangle(img, (0,0), (300,200), (255, 200, 0), 5)
cv2.circle(img, (300,200), 50, (125, 200, 100), 3)
cv2.putText(img, "Hi, man!", (200,180), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)