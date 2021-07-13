# USAGE
# python simple_equalization.py --image images/moon.png

# This uses the cv2.equalizeHist function
# It applies equalisation globally across the entire image rather than 
# piecemeal which is the approach that the adaptive equalisation takes.
# This can lead to washout effects in an image if there is a bright light
# source

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image from disk and convert it to grayscale
print("[INFO] loading input image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization
print("[INFO] performing histogram equalization...")
equalized = cv2.equalizeHist(gray)

# show the original grayscale image and equalized image
cv2.imshow("Input", gray)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)