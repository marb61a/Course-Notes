# USAGE
# python blurring.py

# Covering
# Simple bluring using cv2.blur
# Weighted gaussian blur using cv2.GaussianBlur
# Median filtering using cv2.medianBlur
# Bilateral blurring using cv2.bilateralFilter

# Blurring as most know is when a picture is taken out of focus
# This means that sharper parts of the image use their detail
# The goal is to use a low pass filter to reduce the amount of noise 
# This is done on a practical level by mixing a pixel with surrounding
# pixel intensities, this then becomes the blurred pixel
# This is very useful in image processing altough unwanted in images
# Smoothing and blurring are some of the most common steps in image preprocessing

# Smoothing and blurring are very important operations in computer vision
# This is because by smoothing and blurring images prior to using techniques such as
# edge detection and thresholding, we are able to eliminate noise and other high 
# frequency content such as detail from the image.
# this is done because by removing detail from an image makes objects easier to find

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
	help="path to input image")
args = vars(ap.parse_args())

# load the image, display it to our screen, and initialize a list of
# kernel sizes (so we can evaluate the relationship between kernel
# size and amount of blurring)
# Kernel sizes must be odd so there can be a centre pixel
# The bigger the kernel the more pixels will go into the weighted average
# Be careful with kernel sizes as too big a kernel can over blur which will effect edge detection
# All pixels in the kernel will have an equal weighting
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

# Blurring
# loop over the kernel sizes
for (kX, kY) in kernelSizes:
	# apply an "average" blur to the image using the current kernel
	# size
	blurred = cv2.blur(image, (kX, kY))
	cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# Gaussian Blur
# This is the most used blurring technique
# It is similar to average blurring but instead of using a simple mean
# This time we will use a weighted mean, pixels that are neighbouring 
# and that are closer to the central pixel will contribute more to the 
# weight of the average. This makes the image less blurred but more
# naturally blurred
# loop over the kernel sizes again
for (kX, kY) in kernelSizes:
	# apply a "Gaussian" blur to the image
	# The fianl 0 value instructs OpenCV to automatically compute sigme based on 
	# the kernel size
	blurred = cv2.GaussianBlur(image, (kX, kY), 0)
	cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# Median Blur
# Median blur must have square kernel size whereas the blurring types above
# can have rectangular kernel sizes eg 3, 12
# Salt and pepper noise is black and white pixelated noise
# It is a very unnatural blurring
# loop over the kernel sizes a final time
for k in (3, 9, 15):
	# apply a "median" blur to the image
	blurred = cv2.medianBlur(image, k)
	cv2.imshow("Median {}".format(k), blurred)
	cv2.waitKey(0)