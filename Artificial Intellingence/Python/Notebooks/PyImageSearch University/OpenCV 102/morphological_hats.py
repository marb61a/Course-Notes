# USAGE
# python morphological_hats.py --image car.png

# This file implements the black\top(white) hats

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# TOP HAT
# A top hat is also known as a white hat
# A top hat morphological operation is the difference between the original input image and the opening
# These type of operations are used to reveal bright regions of an image on dark backgrounds
# These operations can be used on greyscale images as well as binary images 

# BLACK HAT
# This is the opposite of a top hat opeation as it will reveal dark regions of an image
# On a light background

# construct a rectangular kernel (13x5) and apply a blackhat
# operation which enables us to find dark regions on a light
# Take special care when defining kernel sizes, these can affect image detection
# Rectangular kernels for example will need much wider than heigher kernels
# background
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# similarly, a tophat (also called a "whitehat") operation will
# enable us to find light regions on a dark background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# show the output images
cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)
