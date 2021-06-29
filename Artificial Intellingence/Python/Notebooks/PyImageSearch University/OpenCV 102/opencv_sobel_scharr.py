# USAGE
# python opencv_sobel_scharr.py --image images/clonazepam_1mg.png

# Text version of tutorial available at the following address
# https://www.pyimagesearch.com/2021/05/12/image-gradients-with-opencv-sobel-and-scharr/ 

# The general idea of thresholding an image is to segment it into foreground and background
# There are other segmentation techniques which are not true segmentation as the idea of segmentation
# impies that every pixel in the image is being segmented. These are what are called edge detection methods
# Instead of labelling every pixel, edge detection will give boundaries. The building blocks of edge
# detection rely on images gradients.

# Image gradients are a fundamental building block of many computer vision and image processing routines
# They can be used as inputs when quantifying images through what is called feature extraction
# Feature extraction are algorithms that automatically quantify the contents of an image for ML etc.
# A very common technique is Histogram of Orientated Gradients (HOG) which combined with Linear SVM
# is a very commonly used object detection method. Saliency maps highlight the subjects of an image

# Edge detection will pick up areas of high contrast on an image, detected edges are called an edge map
# The technical definition of an image gradient is a dieectional change in image intensity
# At each pixel a gradient will measure the change in pixel intensity in any direction. By estimating the 
# direction or orientation along with the magnitude of change we can detect areas of an image that look like edges.

# Using convolutions to detect edges, pixels in the 4 carinal points are the neighbourhood pixels,
# the vertical change is the difference between the north and south pixels, the horizontal change is bewteen east and west 
# Gy and Gx respectively, Gradient magnitude and orientation are reatively  once the Gx and Gy values have been found
# The formula for Gx is --> Gx = I(x + 1, y) – I(x − 1, y)
# The formula for Gy is --> Gy = I(x, y + 1) – I(x, y − 1)
# The gradient magnitude is used to measure how strong the change in image intensity is.
# The gradient orientation is used to determine in which direction the change in intensity is pointing.
# Orientation will give an angle

# To switch to using different kernels when running the file simply change the name that is being added to the command
# For example python opencv_sobel_scharr.py --image images/clonazepam_1mg.png scharr (change to sobel)
# Again it should be stated that the scharr kernel is much more sensitive so will be a lot noisier

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
ap.add_argument("-s", "--scharr", type=int, default=0,
	help="path to input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and display the original
# grayscale image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# When computing the gradient of an image, it is assumed that the image is
# a single channel or grayscale image
cv2.imshow("Gray", gray)

# Sobel Method
# This method uses 2 kernels, one each for horizontal and verical changes in direction
# The Scharr kernel is said to give better approximations to the gradient, these are
# very deep in mathematics

# set the kernel size, depending on whether we are using the Sobel
# operator of the Scharr operator, then compute the gradients along
# the x and y axis, respectively, the -1 value tells that we want to
# use the scharr kernel otherwise we use the value of 3 to tell that we 
# want to use the sobel kernel
ksize = -1 if args["scharr"] > 0 else 3

# This tells that we want a 32 bit floating point data type
# This is to avoid the limitations that would be imposed from working with the usual
# 8 bit unsigned integer
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

# the gradient magnitude images are now of the floating point data
# type, so we need to take care to convert them back a to unsigned
# 8-bit integer representation so other OpenCV functions can operate
# on them and visualize them
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# combine the gradient representations into a single image
# The values give equal weight to gX and gY
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

# show our output images
# The scharr kernel will be much noisier which is because it is much more
# sensitive to gradients changes. Sobel is used a lot however if working
# with images with lots of noise and texture then using the scharr kernel can be very
# beneficial
cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr Y", gY)
cv2.imshow("Sobel/Scharr Combined", combined)
cv2.waitKey(0)
