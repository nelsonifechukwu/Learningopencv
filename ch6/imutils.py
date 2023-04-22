import numpy as np
import cv2

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted  = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, scale):
    (h, w) = image.shape[:2]
    center  = (w//2, h//2) #define the centre of rotation
    M = cv2.getRotationMatrix2D(center, angle, scale) #1.0 here means the scale of the image
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def resize(image, new_width):
    ratio = new_width/image.shape[1]
    dim = (new_width, int(image.shape[0]*ratio))  #(x, y) -> To keep the aspect ratio of the image
    resize_img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resize_img

