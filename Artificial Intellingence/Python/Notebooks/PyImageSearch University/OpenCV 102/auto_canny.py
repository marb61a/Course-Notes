# USAGE
# python auto_canny.py --images images

# The text tutorial version is available at the following url
# https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
# This covers an automatic zero parameter version of the Canny edge detector
# This method works in some cases and not in others as it depends on the dataset
# It uses a simple heuristic but works well in practice.

# import the necessary packages
import numpy as np
import argparse
# The glob package allows for finding file paths on disk
import glob
import cv2

# There are 2 parameters needed, the first is an input image.
# The second parameter is a sigma paramter which helps when calculating the 
# parameters for canny automatic, 0.33 is a value that seems to work well but again
# it can be changed as needed. Lower values result in a tighter edge map and higher
# values the opposite
def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	# Using avg instead of median will increase susceptability to outliers 
	v = np.median(image)

	# apply automatic Canny edge detection using the computed median
	# Values are unsigned 8 bit integers (0 -> 255)
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# return the edged image
	return edged

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input dataset of images")
args = vars(ap.parse_args())

# loop over the images
for imagePath in glob.glob(args["images"] + "/*.jpg"):
	# load the image, convert it to grayscale, and blur it slightly
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (3, 3), 0)

	# apply Canny edge detection using a wide threshold, tight
	# threshold, and automatically determined threshold
	wide = cv2.Canny(blurred, 10, 200)
	tight = cv2.Canny(blurred, 225, 250)
	auto = auto_canny(blurred)

	# show the images
	cv2.imshow("Original", image)
	cv2.imshow("Edges", np.hstack([wide, tight, auto]))
	cv2.waitKey(0)