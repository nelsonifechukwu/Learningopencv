import cv2
import numpy as np

canvas = np.zeros((300,300,3), dtype="uint8")

#Draw a line
red = (0, 0, 255)
green= (0, 255, 0)
cv2.line(canvas, (0,0), (300,300), red)

#Draw a rectangle
cv2.rectangle(canvas, (40,40), (50, 50), green, 40)

#Draw a circle
cx, cy = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255,255,255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (cx, cy), r, white)

cv2.imshow("Drawings", canvas)
cv2.waitKey(0)

