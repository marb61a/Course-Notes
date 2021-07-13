# USAGE
# python adaptive_equalization.py --image images/dog.png

# The text version of the tutorial is available at the following url
# https://www.pyimagesearch.com/2021/02/01/opencv-histogram-equalization-and-adaptive-histogram-equalization-clahe/
# The adaptive version uses the cv2.createCLAHE method

# Histogram and Adaptive Histogram Equalization operate over the histogram of an image, in particular
# a grayscale histogram. They are used to improve the contrast of an image so that images can be 
# better processed. A grayscale image that has been put through an equalizer will have more contrast.

# The way that the algorithm works is by taking a normalised grayscale image histogram and spreading 
# pixels from buckets which have a lot to buckets which have few. In mathematical terms this means 
# that we are attempting to apply a linear trend to our cumulative distribution function

# This also unfortunately boosts the contrast of any noise in the image. We are able however to improve
# contrast without boosting noise by using adaptive histogram equalization. When doing this type of
# equalisation we divide an input image into an M x N grid and then apply equalisation to each cell 
# which gives the output of a higher quality image. This can be complexity from a computing point of view
# but given how powerful modern computer hardware is then both implementations are still quick

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to the input image")
# --clip is for contrtast threshold, default is set to 2.0, OpenCV has a 
# default of 20 but that is not good and a lot of places recommend between
# 2.0 and 4.0
ap.add_argument("-c", "--clip", type=float, default=2.0,
	help="threshold for contrast limiting")
ap.add_argument("-t", "--tile", type=int, default=8,
	help="tile grid size -- divides image into tile x tile cells")
args = vars(ap.parse_args())

# load the input image from disk and convert it to grayscale
print("[INFO] loading input image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
# CLAHE applies a Probability Density Function (PDF)
print("[INFO] applying CLAHE...")
# clipLimit is the threshold for contrast limiting.
# tileGridSize is where the input image is broken into tiles where local equalisation takes place
clahe = cv2.createCLAHE(clipLimit=args["clip"],
	tileGridSize=(args["tile"], args["tile"]))
equalized = clahe.apply(gray)

# show the original grayscale image and CLAHE output image
cv2.imshow("Input", gray)
cv2.imshow("CLAHE", equalized)
cv2.waitKey(0)