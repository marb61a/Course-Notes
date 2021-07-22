# USAGE
# --reference is the path to the refernce image
# python color_correction.py --reference reference.jpg --input examples/01.jpg

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2021/02/15/automatic-color-correction-with-opencv-and-python/

# This chapter is the culmination of the learning that has gone before. We will put together
# a script that will automatically detect and correct colour and lighing issues. The example 
# will use the pantone paint shade color correction card. https://www.pantone.com/eu/en/pantone-color-match-card.
# This will help people detect what colour paint that they want. These cards are the same as photographers cards
# which check colur and their images can be then used in Lightroom to have standardised colour and lighting as
# Photographers and computer vision practitioners can help obtain colour constancy by using colour correction cards

# Images which have almost the same colour can look different due to human perception, the followin address
# is a link to a wikipedia article which explains more -> https://en.wikipedia.org/wiki/Color_constancy.
# There are also some articles which are needed to have been read in order to fully follow the tutorial.
# https://www.pyimagesearch.com/2020/12/14/generating-aruco-markers-with-opencv-and-python/
# https://www.pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/
# https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/

# There is another tutorial available learning more information on four point transform
# https://www.pyimagesearch.com/2016/10/03/bubble-sheet-multiple-choice-scanner-and-test-grader-using-omr-python-and-opencv/

# ArUco markers are 2D binary patterns that computer vision algorithms can easily detect
# These are similar to April Tags which are a type of fiducial marker. Fiducials, or more simply “markers,” 
# are reference objects that are placed in the field of view of the camera when an image or video frame is captured.

# AprilTags are a specific type of fiducial marker, consisting of a black square with a white foreground 
# that has been generated in a particular pattern. There are several benefits to using Aruco over AprilTags.
# ArUco markers are built into the OpenCV library via the cv2.aruco submodule. The OpenCV library itself can generate
# ArUco markers via the cv2.aruco.drawMarker function.  ArUco marker detections tend to be more accurate,
# even when using the default parameters

# import the necessary packages
from imutils.perspective import four_point_transform
from skimage import exposure
import numpy as np
import argparse
import imutils
import cv2
import sys

def find_color_card(image):
	# load the ArUCo dictionary, grab the ArUCo parameters, and
	# detect the markers in the input image
	arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
	arucoParams = cv2.aruco.DetectorParameters_create()
	(corners, ids, rejected) = cv2.aruco.detectMarkers(image,
		arucoDict, parameters=arucoParams)

	# try to extract the coordinates of the color correction card
	try:
		# otherwise, we've found the four ArUco markers, so we can
		# continue by flattening the ArUco IDs list
		ids = ids.flatten()

		# extract the top-left marker
		i = np.squeeze(np.where(ids == 923))
		topLeft = np.squeeze(corners[i])[0]

		# extract the top-right marker
		i = np.squeeze(np.where(ids == 1001))
		topRight = np.squeeze(corners[i])[1]

		# extract the bottom-right marker
		i = np.squeeze(np.where(ids == 241))
		bottomRight = np.squeeze(corners[i])[2]

		# extract the bottom-left marker
		i = np.squeeze(np.where(ids == 1007))
		bottomLeft = np.squeeze(corners[i])[3]

	# we could not find color correction card, so gracefully return
	except:
		return None

	# build our list of reference points and apply a perspective
	# transform to obtain a top-down, birds-eye-view of the color
	# matching card
	cardCoords = np.array([topLeft, topRight,
		bottomRight, bottomLeft])
	card = four_point_transform(image, cardCoords)

	# return the color matching card to the calling function
	return card

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--reference", required=True,
	help="path to the input reference image")
ap.add_argument("-i", "--input", required=True,
	help="path to the input image to apply color correction to")
args = vars(ap.parse_args())

# load the reference image and input images from disk
print("[INFO] loading images...")
ref = cv2.imread(args["reference"])
image = cv2.imread(args["input"])

# resize the reference and input images
# Can be change if higher resolution images are being sought
ref = imutils.resize(ref, width=600)
image = imutils.resize(image, width=600)

# display the reference and input images to our screen
cv2.imshow("Reference", ref)
cv2.imshow("Input", image)

# find the color matching card in each image
print("[INFO] finding color matching cards...")
refCard = find_color_card(ref)
imageCard = find_color_card(image)

# if the color matching card is not found in either the reference
# image or the input image, gracefully exit
if refCard is None or imageCard is None:
	print("[INFO] could not find color matching card in both images")
	sys.exit(0)

# show the color matching card in the reference image and input image,
# respectively
cv2.imshow("Reference Color Card", refCard)
cv2.imshow("Input Color Card", imageCard)

# apply histogram matching from the color matching card in the
# reference image to the color matching card in the input image
print("[INFO] matching images...")
imageCard = exposure.match_histograms(imageCard, refCard,
	multichannel=True)

# show our input color matching card after histogram matching
cv2.imshow("Input Color Card After Matching", imageCard)
cv2.waitKey(0)