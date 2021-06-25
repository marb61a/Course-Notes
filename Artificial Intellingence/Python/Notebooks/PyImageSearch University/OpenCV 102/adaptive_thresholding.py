# USAGE
# python adaptive_thresholding.py --image steve_jobs.png

# Using cv2.adaptiveThreshold
# Text tutorial available at the following address
# https://www.pyimagesearch.com/2021/05/12/adaptive-thresholding-with-opencv-cv2-adaptivethreshold/
# Adaptive thresholding has a notion of locality
# T may need a different value for different parts of an image
# In Otsu T is applied globally which may not be a good approach
# When there are things like shadows or non-uniform lightng conditions then
# having one value of T for an image will not suffice
# Adaptive thresholding considers small neighbours of pixels and finds am optimal 
# value of T which is then applied. Adaptive thresholding is also sometimes
# known as local thresholding. Adaptive\Local thresholding makes an assumption
# and that is that smaller regions of an image are likely to have uniform
# lighting or illumination. Local regions will have similar illumination
# where as the larger image will have different illuminations

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Image", image)

# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# Simple Thresholding
# apply simple thresholding with a hardcoded threshold value
(T, threshInv) = cv2.threshold(blurred, 230, 255,
	cv2.THRESH_BINARY_INV)
cv2.imshow("Simple Thresholding", threshInv)
cv2.waitKey(0)

# Otsu Thresholding
# apply Otsu's automatic thresholding
(T, threshInv) = cv2.threshold(blurred, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Otsu Thresholding", threshInv)
cv2.waitKey(0)

# Adaptive Thresholding
# instead of manually specifying the threshold value, we can use
# adaptive thresholding to examine neighborhoods of pixels and
# adaptively threshold each neighborhood
# The first parameter is the blurred input image
# The second parameter is the output threshold value (as seen previously)
# The third parameter is the adaptive threshold method, in this case mean c is used
# to indicate using the local pixel neighbourhood to compute T threshold value
# 10 is the constant value that can be subtracted from the mean, this can be changed
# to suit images
thresh = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
cv2.imshow("Mean Adaptive Thresholding", thresh)
cv2.waitKey(0)

# perform adaptive thresholding again, this time using a Gaussian
# weighting versus a simple mean to compute our local threshold
# value. Similar to the gaussian approach in blurring, this may be a more
# natural approach and there is a difference between this method and the mean method
# When flags are switched then things like the C value, in this case 4 will probably need
# to be changed.
thresh = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
cv2.imshow("Gaussian Adaptive Thresholding", thresh)
cv2.waitKey(0)