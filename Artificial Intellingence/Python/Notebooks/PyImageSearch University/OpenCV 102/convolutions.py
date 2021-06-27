# USAGE
# python convolutions.py --image 3d_pokemon.png

# Text version of the tutorial available at the following url
# https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/
# Image convolution is not a complicatd term and having done dome of the tutorials up until
# this point the student has already applied convolutions. This is because blurring and smoothing
# are convolutions. Other things that are convolutions are sharpening an image in Gimp or other program
# Convolutions are one of the most critical, fundamental building-blocks in computer vision and 
# image processing. An image convolution in reality is simply an element-wise multiplication of 
# two matrices followed by a sum. An image is simply a multi-dimensional matrix. RGB images show
# that unlike school matrices image matrices have depth, in the case of RGB there is a depth of 3.
# An image can be thought of as a big matrix and a kernel as a tiny matrix. The tiny kernel sits 
# on top of the big image and slides from left-to-right and top-to-bottom, applying a mathematical 
# operation at each coordinate of the image. Blurring, sharpening and edge detection are all forms of 
# hand-defined kernels that are specifically designed to perform a particular function.

# Kernels can be an arbitrary size of M x N pixels, provided that both M and N are odd integers
# In a lot of kernels however it is usually N x N pixels which are square. Again odd number size
# is used to ensure that there is a proper integer number coordinate at the image centre.

# Performing a convolution is fairly easy, the first thing is to select an x, y coordinate from the
# original image. This coorinate would then be where the centre of the kernel is placed. Then
# take the element-wise multiplication of the input image region and the kernel and sum the values
# of the multiplication operations into a single value called the kernel output.

# import the necessary packages
# scikit image may need to be installed using pip
from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

# Building a custom convolve method
def convolve(image, kernel):
	# grab the spatial dimensions of the image, along with
	# the spatial dimensions of the kernel
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]

	# allocate memory for the output image, taking care to
	# "pad" the borders of the input image so the spatial
	# size (i.e., width and height) are not reduced
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")

	# Important to understand sliding, when sliding a convolutional matrix
	# across an image and applying a convolution and storing the output. This
	# will actually decrease the the spatial dimensions of the output image. 
	# This is down to the fact that computation is centered around the centre x, y
	# coordinate that the input image that the kernel is currently positioned over.
	# This implies there is no such thing as “center” pixels for pixels that fall 
	# along the border of the image so the decrease in spatial dimensions is a side
	# effect of this, this can be good or bad depending on application
	# loop over the input image, "sliding" the kernel across
	# each (x, y)-coordinate from left-to-right and top to
	# bottom
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			# extract the ROI of the image by extracting the
			# *center* region of the current (x, y)-coordinates
			# dimensions
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

			# perform the actual convolution by taking the
			# element-wise multiplicate between the ROI and
			# the kernel, then summing the matrix
			k = (roi * kernel).sum()

			# store the convolved value in the output (x,y)-
			# coordinate of the output image
			output[y - pad, x - pad] = k

	# rescale the output image to be in the range [0, 255]
	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")

	# return the output image
	return output

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# construct average blurring kernels used to smooth an image
smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

# Kernel Construction
# construct a sharpening filter
# The sharpening kernel is used to enhance line structures and other details 
# of an image
sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")

# construct the Laplacian kernel used to detect edge-like
# regions of an image
laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")

# construct the Sobel x-axis kernel
# Used to detect vertical changes in the gradient of the image
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")

# construct the Sobel y-axis kernel
# Used to detect horizontal changes in the gradient
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")

# construct the kernel bank, a list of kernels we're going
# to apply using both our custom `convole` function and
# OpenCV's `filter2D` function
kernelBank = (
	("small_blur", smallBlur),
	("large_blur", largeBlur),
	("sharpen", sharpen),
	("laplacian", laplacian),
	("sobel_x", sobelX),
	("sobel_y", sobelY)
)

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# loop over the kernels
for (kernelName, kernel) in kernelBank:
	# apply the kernel to the grayscale image using both
	# our custom `convole` function and OpenCV's `filter2D`
	# function
	print("[INFO] applying {} kernel".format(kernelName))
	convoleOutput = convolve(gray, kernel)
	opencvOutput = cv2.filter2D(gray, -1, kernel)

	# show the output images
	cv2.imshow("original", gray)
	cv2.imshow("{} - convole".format(kernelName), convoleOutput)
	cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
	cv2.waitKey(0)
	cv2.destroyAllWindows()