import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

parse = argparse.ArgumentParser(description = "get the image")
parse.add_argument("-i", "--image", required = True, help="specify image path")
args = vars (parse.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image",image)

'''
Blurring helps to remove noise from the image
like a moving average filter

'''

blurred = np.hstack([cv2.blur(image, (3,3)), 
                              cv2.GaussianBlur(image, (5,5), 0),
                              cv2.bilateralFilter(image, 3)])

cv2.imshow("Average", blurred)
cv2.waitKey(0)