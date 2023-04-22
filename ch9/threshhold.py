#convert a grayscale image to a binary image 
#where the pixels are either 0 or 255

#E.g set a threshold value p where all values < p = 0
#and all values > p = 255

#we threshold to focus on particular areas of an object
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

parse = argparse.ArgumentParser(description = "get the image")
parse.add_argument("-i", "--image", required = True, help="specify image path")
args = vars (parse.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image",image)

blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Blurred Image",blurred)

gscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(T, thresh) = cv2.threshold(gscale_img, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(gscale_img, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThresholdInv Binary", threshInv)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 3)


cv2.waitKey(0)