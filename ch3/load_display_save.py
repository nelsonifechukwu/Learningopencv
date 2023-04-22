#Command is the specific program/subroutine executed in the CLI
#Option is an optional argument that modifies the command's behavior
#Argument is an optional or required info that a command uses to perform its function
#Parameter is an argument that an option uses to perform its function

   ## See sys.argv
#sys.argv = [name of command, directory to perform command]

from __future__ import print_function
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="Path to the image")
#args = vars(ap.parse_args())


image = cv2.imread("ch3/trex.png")

#edit pixels of an image
image [0:100, 0:100] = (0, 255, 0)

#print details of an image
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey(0)

#save the image as a png
cv2.imwrite("ch3/tre.png", image)
