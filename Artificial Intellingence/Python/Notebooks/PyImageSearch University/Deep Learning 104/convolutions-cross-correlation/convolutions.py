# USAGE
# python convolutions.py --image jemma.png

# The text version of the tutorial is available at the following url
# https://www.pyimagesearch.com/2021/05/14/convolution-and-cross-correlation-in-neural-networks/

# The tutorial is about convolution and cross-correlation and the role thay they play in Neural
# Networks. Every thing that has been done thus far has led to this point which is to understand
# Convolutional Neural Networks (CNNs) and the role they play in deep learning. It is also 
# important that students have completed the OpenCV 102 section and more precisely the kernels 
# video and text tutorial. This is because convolution is dicussed in terms of images which will
# lead on to this discussion which will cover convolution and neural networks. 

# In order to understand what exactly is convolution we should understand the role that it plays.
# Convolution itself is not really a complicated term although it sounds very technical. Convolutions
# on images for example are blurring, sharpening etc, these are some of the most important building
# blocks in computer vision. In deep learning a convolution is the elementwise multiplication of 
# 2 matrices followed by a sum. That is all, take 2 matices of the same dimension and multiply them
# element by element and sum the elements together.

# In traditional feedforward neural networks, each neuron in the input layer is connected to every 
# output neuron in the next layer — we call this a fully connected (FC) layer. In CNN's however
# a fully connected layer is not used until the very last layer in the network. This means that a 
# CNN can be defined as a neural network that swaps in a specialized “convolutional” layer in place
# of “fully connected” layer for at least one of the layers in the network. A non-linear activation
# function such as Re-LU can then be applied  to the output of these convolutions and the process of 
# convolution => activation continues until the end of the network is reached. Then the FC layer(s) 
# can be applied to obtain our final output classifications. Each layer in a CNN applies a different 
# set of filters, there could be hundereds or thousands of these which combines the outputs and sends
# the output to the next layer. During training, a CNN automatically learns the values for these filters.
# In the context of images a CNN can learn to detect edges from raw pixel data in the first layer, then 
# use these edges in the second layer to detect shapes, in the next layers these can be used to detect
# higher-level features. The last layer in a CNN uses these higher-level features to make predictions 
# regarding the contents of the image. CNN's give 2 key benefits, the first is local invariance which
# allows us to classify an image as containing a particular object regardless of where in the image the 
# object appears. This local invariance is obtained through pooling layers which is where regions of our 
# input volume are identified with a high response to a particular filter. The second benefit is 
# composability which is where a filter composes a local patch of lower-level features into a higher-level
# representation. This is similar to when building a set of mathematical functions that build on the output 
# of previous functions. The concept of building higher-level features from lower-level ones is exactly why 
# CNNs are so powerful in computer vision. This also means that CNN's and NN's in general have hierarchies.

# There are a lot of times where cross-correlation is used rather than convolution. Most deep learning
# libraries use the simplified cross-correlation operation and call it convolution. 

# To see more on Kernels, check out the notes at the following url
# https://github.com/marb61a/Course-Notes/blob/master/Artificial Intellingence/Python/Notebooks/PyImageSearch University/OpenCV 102/convolutions.py

# import the necessary packages
# Scales the convolution output
from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

# Performs the convolution, K is the filter that will be applied
def convolve(image, K):
	# grab the spatial dimensions of the image and kernel
	(iH, iW) = image.shape[:2]
	(kH, kW) = K.shape[:2]

	# allocate memory for the output image, taking care to "pad"
	# the orders of the input image so the spatial size (i.e.,
	# width and height) are not reduced
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float")

	# loop over the input image, "sliding" the kernel across
	# each (x, y)-coordinate from left-to-right and top-to-bottom
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			# extract the ROI of the image by extracting the
			# *center* region of the current (x, y)-coordinates
			# dimensions
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

			# perform the actual convolution by taking the
			# element-wise multiplication between the ROI and
			# the kernel, the summing the matrix
			k = (roi * K).sum()

			# store the convolved value in the output (x, y)-
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

# construct a sharpening filter
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
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")

# construct the Sobel y-axis kernel
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")

# construct an emboss kernel
emboss = np.array((
	[-2, -1, 0],
	[-1, 1, 1],
	[0, 1, 2]), dtype="int")

# construct the kernel bank, a list of kernels we're going to apply
# using both our custom `convole` function and OpenCV's `filter2D`
# function
kernelBank = (
	("small_blur", smallBlur),
	("large_blur", largeBlur),
	("sharpen", sharpen),
	("laplacian", laplacian),
	("sobel_x", sobelX),
	("sobel_y", sobelY),
	("emboss", emboss))

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# loop over the kernels
for (kernelName, K) in kernelBank:
	# apply the kernel to the grayscale image using both our custom
	# `convolve` function and OpenCV's `filter2D` function
	print("[INFO] applying {} kernel".format(kernelName))
	convolveOutput = convolve(gray, K)
	opencvOutput = cv2.filter2D(gray, -1, K)

	# show the output images
	cv2.imshow("Original", gray)
	cv2.imshow("{} - convole".format(kernelName), convolveOutput)
	cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
