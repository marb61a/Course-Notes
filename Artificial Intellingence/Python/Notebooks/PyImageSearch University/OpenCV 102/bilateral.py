# USAGE
# python bilateral.py

# This is more complicated than using just blurring
# Blurring has been used to reduce detail and noise in an image
# To keep the noise use bilateral blurring
# Bilateral blurring ases 2 Gaussian distributions to accomplish this. 
# The first distibution considers only yhte spatial neighbours which are
# pixels that appear close together in the coordinate space of the image
# The second distribution then models the neighbourhood pixel intensity to
# ensure that only pixels with similar intensity are include in the blur computing 

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
	help="path to input image")
args = vars(ap.parse_args())

# load the image, display it to our screen, and construct a list of
# bilateral filtering parameters that we are going to explore
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
	# apply bilateral filtering to the image using the current set of
	# parameters
	# The first parameter is the image being processed
	# The second parameter is the diameter of the pixel neighbourhood, 
	# the larger the diameter the more pixels are included in the blurring computation
	# The third parameter is ther color standard deviation. A larger value means that
	# more colours in the neighbourhood will be considered when computing the blur
	# The fourth parameter is the space standard deviation, a larger value means
	# that pixels further from the central pixel will be considered when computing the blur
	blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)

	# show the output image and associated parameters
	title = "Blurred d={}, sc={}, ss={}".format(
		diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
	cv2.waitKey(0)