import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import imutils

parse = argparse.ArgumentParser(description = "get the image")
parse.add_argument("-i", "--image", required = True, help="specify image path")
args = vars (parse.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image",image)

#Translation
shifted_img = imutils.translate(image, 100, 7)
#cv2.imshow("translated_img", shifted_img)

#Rotation
#You can rotate about a center by using a rotation matrix
rotated_img = imutils.rotate(image, 45, 1.0)
#cv2.imshow("rotated_img", rotated_img)

#Resize image
resized_img = imutils.resize(image, 100)
#cv2.imshow("resized_img", resized_img)

#Flipping image
flip_img = cv2.flip(image, 1)
#cv2.imshow("flipped_img", flip_img)

#Cropped image
cropped_img = image[0: 100, 0:100]

#Adding & subtracting to image
M = np.zeros(image.shape, dtype="uint8") * 100
added = cv2.add(image, M) # see also np.
#cv2.imshow("added", added)

#Image masking
mask = np.ones(image.shape[:2], dtype = "uint8")
(cx, cy) = (image.shape[1]//2, image.shape[0]//2)
cv2.circle(mask, (cx, cy), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
#cv2.imshow("Mask", mask)
#cv2.imshow("Mask Applied to Image", masked)

#splitting and merging images
(b, g, r) = cv2.split(image)
print(b, g, r)

#Histogram
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("Flattened Histogram per Channel")
plt.xlabel("Bins")
plt.ylabel("No of bins")

for chan, color in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.show()

cv2.waitKey(0)






