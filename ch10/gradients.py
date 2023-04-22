import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

parse = argparse.ArgumentParser(description = "get the image")
parse.add_argument("-i", "--image", required = True, help="specify image path")
args = vars (parse.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image",image)


#Laplacian and sobel helps us to calculate the gradients on images so that
#we can find the edges in the image 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(image, cv2.CV_64F)
#we use 64 bits here to represent negative values got from the laplacian calculation
#else, opencv will clip them and we'll lose our edges
lap = np.uint8(np.absolute(lap))

#Sobel
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY) 

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)

cv2.imshow("Sobel Combined", sobelCombined)
cv2.imshow("gradient", lap)

#Canny edge detection

'''
Canny edge detection is a multistage process that involves
blurring the image to remove noise (like moving average), computing the sobel gradients, 
supressing egdes and finally a hysteresis thresholding

'''
image = cv2.GaussianBlur(image, (5,5), 0)
canny = cv2.Canny(image, 30,150)
cv2.imshow("Canny", canny)

#30 and 150 are thresholds, 
cv2.waitKey(0)
