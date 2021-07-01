# USAGE
# python opencv_canny.py --image images/coins.png

# Tutorial uses the cv2.Canny method
# Text version of the tutorial is available from the following
# https://www.pyimagesearch.com/2021/05/12/opencv-edge-detection-cv2-canny/

# Canny is a classic in the computer vision world, it is a fairly fundamental
# part of learning computer vision. It is not a trivial process to understand
# the algorithm. It is so well used that cv2 has its own implementation using
# cv2.Canny. It is named after John Canny and his paper is available at
# https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.420.3300&rep=rep1&type=pdf

# There is a 4 step process to Canny Edge Detection -> Gaussian smoothing,
# Computing the gradient magnitude and orientation, Non-maxima suppression
# and Hysteresis thresholding

# Using formal language an edge is defined as discontinuities in pixel intensity, 
# or more simply, a sharp difference and change in pixel values. A step edge forms 
# when there is an abrupt change in pixel intensity from one side of the discontinuity to the other.
# As is to be expected these types of edges tend to be easy to detect. A ramp edge is like a step edge, 
# only the change in pixel intensity is not instantaneous. Instead, the change in pixel value occurs a 
# short, but finite distance. A ridge edge is similar to combining two ramp edges, one bumped right 
# against another. Finally we have the roof edge, which is a type of ridge edge.

# Similar to segmenting the goal of edge detection
# is to be able to seperate the foreground from the background. It is more specific
# than segementing as we are looking at the boundary between objects. Canny relies
# on image gradients. When looking at edge detection the gradient magnitude is
# extremely sensitive to noise. An image that has become an edge map is a binary
# image, either black or white. Hysteresis thresholding is going to where a lot of time 
# is spent tuning parameters.

# There is also a process when applyting the actual algorithm
# Firstly is applying Gaussian smoothing to the image to help reduce noise
# The second step is to compute the image gradients using the Sobel kernel
# The third step then is applying non-maxima suppression to keep only the local maxima of 
#	gradient magnitude pixels that are pointing in the direction of the gradient
#	Maxima thresholding is not that complicated a process, it is simply edge thinning
# The fourth is applying upper and lower thresholds for Hysteresis thresholding
#	this is where we remove things that are not edges but respond like edges

# Setting edge thresholds can be very difficult, too loose and there will be a lot of edges
# detected. On the otherhand if there is too tight a threshold then there may not be enough
# edges detected. It is important to not get frustrated in the process. There are 3 different 
# edgemaps that can be used wide, mid and tight. There is an automatic version available
# for when manually trying and testing is not feasible.

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# show the original and blurred images
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

# compute a "wide", "mid-range", and "tight" threshold for the edges
# using the Canny edge detector
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

# show the output Canny edge maps
cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)
