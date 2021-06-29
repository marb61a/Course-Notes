# USAGE
# python opencv_magnitude_orientation.py --image images/coins02.png

# This script is for computing both the Gradient Magnitude and also the
# Gradient Orientation 

# import the necessary packages
# Matplotlib will allow for displaying some figures with good formatting
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute gradients along the x and y axis, respectively
# Although using a 64 bit floating point a 32 bit number can be used
# equally as well
gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

# compute the gradient magnitude and orientation
# The magnitude is squaring both gX and gY and adding them and then taking
# the square root
magnitude = np.sqrt((gX ** 2) + (gY ** 2))
# Orientation is the arc tangent between gY and gX and then convert to degrees
# The modulus operation will give either a signed or unsigned gradient
# This will be seen more when studying image histograms, HOG etc
# The 180 will clamp degree values between 0 and 180 rather than 360
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

# initialize a figure to display the input grayscle image along with
# the gradient magnitude and orientation representations, respectively
(fig, axs) = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))

# plot each of the images
# Uses the Jet colour map, more information can be found at
# https://stackoverflow.com/questions/7440340/jet-colormap-to-grayscale
axs[0].imshow(gray, cmap="gray")
axs[1].imshow(magnitude, cmap="jet")
axs[2].imshow(orientation, cmap="jet")

# set the titles of each axes
axs[0].set_title("Grayscale")
axs[1].set_title("Gradient Magnitude")
axs[2].set_title("Gradient Orientation [0, 180]")

# loop over each of the axes and turn off the x and y ticks
for i in range(0, 3):
	axs[i].get_xaxis().set_ticks([])
	axs[i].get_yaxis().set_ticks([])

# show the plots
plt.tight_layout()
plt.show()
