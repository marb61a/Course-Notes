# USAGE
# python adjust_gamma.py --image /images/example_01.png

# Text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/

# Human eyes and cameras perceive color and luminance differently. 
# When twice the number of photons hit the sensor of a digital camera, it receives twice 
# the signal. This differes from how eyes work, human eyes perceive double the amount
# of ligtht as only a fraction brighter. Human eyes are also much more sensitive
# to any changes in dark tones rather than bright ones.

# Gamma correction is a common image editing process if you are seeking
# to change the luminence of an image. Gamma correction can be thought of as a translation
# between the sensitivity of our eyes and sensors of a camera.

# Gamma correction is also known as the Power Law Transform. Firstly image pixel intensities
# must be scaled from the range [0, 255] to [0, 1.0] Then thr following equation is applied
# O = I ^ (1 / G) which gives the output gamma corrected image. Where I is our input image 
# and G is our gamma value. The output image O is then scaled back to the range [0, 255]. 
# Gamma values < 1 will shift the image towards the darker end of the spectrum while
# gamma values > 1 will make the image appear lighter. A gamma value of G=1 will have no affect
# on the input image

# import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import cv2

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the original image
original = cv2.imread(args["image"])

# loop over various values of gamma
for gamma in np.arange(0.0, 3.5, 0.5):
	# ignore when gamma is 1 (there will be no change to the image)
	if gamma == 1:
		continue

	# apply gamma correction and show the images
	gamma = gamma if gamma > 0 else 0.1
	adjusted = adjust_gamma(original, gamma=gamma)
	cv2.putText(adjusted, "g={}".format(gamma), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.imshow("Images", np.hstack([original, adjusted]))
	cv2.waitKey(0)