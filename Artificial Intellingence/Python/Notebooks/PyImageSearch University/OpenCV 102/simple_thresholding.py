# USAGE
# python simple_thresholding.py --image images/coins01.png

# The accompanying text tutorial is available at
# https://www.pyimagesearch.com/2021/04/28/opencv-thresholding-cv2-threshold/
# Thresholding is a basic image segmentation technique
# The goal is to segment an image into foreground and background pixels/objects
# Thresholding is used a lot in computer vision and image processing
# The biggest pain using this type of thresholding is that you have to
# manually set the threshold value, it will require a lot of experimentation
# and can be difficult to be successful. There may be occasions when due to
# lighting parts of images may need different thresholds

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

# When thresholding an image it will be grayscale or a single channel image
# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Removes the high frequency noise and smoothes out details
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# apply basic thresholding -- the first parameter is the image
# we want to threshold, the second value is is our threshold
# check; if a pixel value is greater than our threshold (in this
# case, 200), we set it to be *black, otherwise it is *white*
# Typically when constructing an image we will want black pixels as the background
# and white as the foreground, the final parameter is usually set to 255
(T, threshInv) = cv2.threshold(blurred, 200, 255,
	cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

# using normal thresholding (rather than inverse thresholding)
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

# visualize only the masked regions in the image using bitwise
# operations (foreground region)
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)