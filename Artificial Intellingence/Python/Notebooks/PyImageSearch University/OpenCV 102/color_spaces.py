# USAGE
# python color_spaces.py

# Text tutorial accompanying the video
# https://www.pyimagesearch.com/2021/04/28/opencv-color-spaces-cv2-cvtcolor/

# Colour spaces can be an overlooked topice for computer vision newbies
# Working with colour space can be the difference between a successful project
# and a failed project. This uses the cv2.cvtColor() method
# There are 3 goals when working with lighting conditions which are very closely
# related to colour spaces. 
# High Contrast between back and foreground, if this is not the case then it will be
# a challenge to process the image. High contrast should be sought out in order
# to be able to see boundaries.
# Generalizable, under different lighting conditions an object is going to look 
# different however conditions should be consistent enough to work from one object to the next 
# Stable, The quality of light maybe the most important factor in getting image accuracy
# stable along with consistent and repeatable lighting conditions are the holy grail
# of cv app development. It is however extremely difficult to guarantee

# There are 4 main colour spaces encountered when doing computer vision
# RGB, HSV, L*a*b* and Grayscale

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
	help="path to input image")
args = vars(ap.parse_args())

# RGB Space
# load the original image and show it
image = cv2.imread(args["image"])
cv2.imshow("RGB", image)

# loop over each of the individual channels and display them
# BGR channeling was the standard when OpenCV was developed
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
	cv2.imshow(name, chan)

# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()


# HSV Space
# H -> Hue, S -> Saturation, V -> Value
# convert the image to the HSV color space and show it
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# loop over each of the invidiaul channels and display them
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
	cv2.imshow(name, chan)

# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()


# L*a*b* Space
# Is better at modelling how humans see colour
# convert the image to the L*a*b* color space and show it
# Difference in colour hs perceptual meaning unlike RGB and HSV
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

# loop over each of the invidiaul channels and display them
for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
	cv2.imshow(name, chan)

# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Grayscale space
# Grayscale is not really a colur space
# show the original and grayscale versions of the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)