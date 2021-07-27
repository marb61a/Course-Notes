# USAGE
# python opencv_generate_aruco.py --id 24 --type DICT_5X5_100 --output tags/DICT_5X5_100_id24.png

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2020/12/14/generating-aruco-markers-with-opencv-and-python/

# ArUco makers are similar to AprilTags as they are 2D binary patterns that computer vision 
# algorithms can easily detect. They also have very similar use cases and can be used in
# Robotics, Camera Calibration etc which makes then very important in Computer vision.
# The patterns that make up an ArUco tag are fairly easy to tell that they are generated
# rather than something that occurs naturally. 

# There are some advantages to using ArUco tags instead of AprilTags such as 
# ArUco markers are built into the OpenCV library via the cv2.aruco submodule 
# (i.e., we don’t need additional Python packages). The OpenCV library itself can generate
# ArUco markers via the cv2.aruco.drawMarker function. There are online ArUco generators that
# can be used if there is a reason not to do coding.

# Learning to generate your own tags is a necessary step in order to be able to understand
# where to place them in your process. An ArUco dictionary specifies the type of ArUco marker 
# we are generating and detecting, without the dictionary we would be unable to generate and 
# detect these markers

# Deciding on which ArUco dictionary to use has a few different factors. The first is to 
# consider how many unique values are needed. If a smaller number of values is needed then
# use a smaller dictionary and do not take more than is needed. Examine the input image or
# video size, the larger the grid size gets then the larger the ArUco marker will need to be.
# One thing to note is that if using a large grid but low resolution output then markers may
# not be detectable. The final thing to consider is the inter marker distance smaller dictionary
# sizes with larger NxN marker sizes increase the inter-marker distance, thereby making them 
# less prone to false readings

# There are some ideal settings
# A low number of unique ArUco IDs that need to be generated and read
# High-quality image input containing the ArUco markers that will be detected
# A larger NxN grid size, balanced with a low number of unique ArUco IDs such that the inter-marker 
# distance can be used to correct misread markers

# import the necessary packages
import numpy as np
import argparse
import cv2
# Needed if we neeed to exit the script
import sys

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output image containing ArUCo tag")
ap.add_argument("-i", "--id", type=int, required=True,
	help="ID of ArUCo tag to generate")
ap.add_argument("-t", "--type", type=str,
	default="DICT_ARUCO_ORIGINAL",
	help="type of ArUCo tag to generate")
args = vars(ap.parse_args())

# define names of each possible ArUco tag OpenCV supports
# OpenCV provides support for about 21 different marker dictionaries 
# The numbers 50, 100 etc are the maximum available number of id's
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

# verify that the supplied ArUCo tag exists and is supported by
# OpenCV
if ARUCO_DICT.get(args["type"], None) is None:
	print("[INFO] ArUCo tag of '{}' is not supported".format(
		args["type"]))
	sys.exit(0)

# load the ArUCo dictionary
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])

# allocate memory for the output ArUCo tag and then draw the ArUCo
# tag on the output image
print("[INFO] generating ArUCo tag type '{}' with ID '{}'".format(
	args["type"], args["id"]))
tag = np.zeros((300, 300, 1), dtype="uint8")
cv2.aruco.drawMarker(arucoDict, args["id"], 300, tag, 1)

# write the generated ArUCo tag to disk and then display it to our
# screen
cv2.imwrite(args["output"], tag)
cv2.imshow("ArUCo Tag", tag)
cv2.waitKey(0)