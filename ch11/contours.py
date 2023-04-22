import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

parse = argparse.ArgumentParser(description = "get the image")
parse.add_argument("-i", "--image", required = True, help="specify image path")
args = vars (parse.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image",image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (15,15), 0)

canny = cv2.Canny(image, 30,160)
cv2.imshow("Canny", canny)

'''
Contours helps you to outline and group pixels of the same intensity level
as objects in an image
'''
(contours, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(len(contours))
#Draw the contours on the image
coins = image.copy()

#convert the image back to RGB
coins = cv2.cvtColor(coins, cv2.COLOR_GRAY2BGR)
cv2.drawContours(coins, contours, -1, (0, 255, 0), 2)
cv2.imshow("contour", coins)
#30 and 150 are thresholds

#count the coins
for (i, c) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)

print("Coin #{}".format(i + 1))
coin = image[y:y + h, x:x + w]
cv2.imshow("Coin", coin)

mask = np.zeros(image.shape[:2], dtype = "uint8")


((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
cv2.circle(mask, (int(centerX), int(centerY)), int(radius),255, -1)
mask = mask[y:y + h, x:x + w]
cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))

cv2.waitKey(0)
