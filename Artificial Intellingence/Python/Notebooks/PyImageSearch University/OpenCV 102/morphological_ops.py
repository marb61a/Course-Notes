# USAGE
# python morphological_ops.py --image pyimagesearch_logo.png

# Will be looking at several different morphological operations
# Erosion
# Dilations
# Open & Closing
# Morphological Gradient
# Black Hat & Top Hat (AKA White hat)

# Morphological are a fundamental part of image processing
# they are used to clean up images prior to further proceses
# These operations can obviate having to use other DL/ML/AI tools

# Removing white patches from an image

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and display it to our
# screen
# This will automatically remove the white background marks in the image
# The image is a binary value image (b/w)
# Images should be changed to binary images as quick as possible
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# EROSION
# Erosion in an image erodes the the foreground image and makes it smaller
# Pixels near to the boundary of an object will be discarded
# Erosion works by defining a structuring element and then sliding the structuring element
# from l->r and t->b across the input image
# A foreground pixel will only be kept if all the pixels insode the structuring element are > 0
# Erosion is performed using the cv2.erode() function 
# apply a series of erosions
for i in range(0, 3):
	# None refers to kernels, there are several 3 * 3 is used by default
	# Each erosion will make the image letters disappear
	# When used elsewhere it can help eliminate items which are seperate but appear connected
	eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
	cv2.imshow("Eroded {} times".format(i + 1), eroded)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# DILATIONS
# This is the opposite of erosion as instead of eroding pixels in the foreground
# dilations will add to or grow foreground pixels
# apply a series of dilations
# Lettering in the image will enlarge to the point of touching
# Dilations are used typically after a series of erosions
for i in range(0, 3):
	dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
	cv2.imshow("Dilated {} times".format(i + 1), dilated)
	cv2.waitKey(0)

# close all windows to cleanup the screen, then initialize a list of
# of kernels sizes that will be applied to the image
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# Explicity creates kernel sizes for using in morphological operations
kernelSizes = [(3, 3), (5, 5), (7, 7)]

# OPENING
# An opening is an erosion folwed by a dilation
# This can be used to remove small blobs from an image
# First eh erosion is applied then the dilation to grow back the original project size

# loop over the kernels sizes
for kernelSize in kernelSizes:
	# construct a rectangular kernel from the current size and then
	# apply an "opening" operation
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Opening: ({}, {})".format(
		kernelSize[0], kernelSize[1]), opening)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# CLOSING
# As is to be expected a closing is the exact opposite of an opening
# loop over the kernels sizes again
for kernelSize in kernelSizes:
	# construct a rectangular kernel form the current size, but this
	# time apply a "closing" operation
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
	cv2.imshow("Closing: ({}, {})".format(
		kernelSize[0], kernelSize[1]), closing)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# Morpholoigcal Gradient
# This is the difference between a dialtion and an erosion
# It is used when detemining the outline of a particular object of an image
# It can be thought of as a boundary detector
# loop over the kernels a final time
for kernelSize in kernelSizes:
	# construct a rectangular kernel and apply a "morphological
	# gradient" operation to the image
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
	cv2.imshow("Gradient: ({}, {})".format(
		kernelSize[0], kernelSize[1]), gradient)
	cv2.waitKey(0)