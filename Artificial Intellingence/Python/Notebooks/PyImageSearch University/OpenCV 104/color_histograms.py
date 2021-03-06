# USAGE
# python color_histograms.py --image beach.png

# The text version of the tutorial is available at the following url
# https://www.pyimagesearch.com/2021/04/28/opencv-image-histograms-cv2-calchist/
# We will use the cv2.calcHist function.

# Histograms are used in nearly every aspect of computer vision and there are 
# different types, greyscale histograms are used for thresholding, ordinary histograms 
# are used for white balancing. Color histograms are used for object tracking in images
# and se algorithms such as the CamShift algorithm. Color histograms can also be used
# as features which alows for including image histograms in multiple dimensions

# In an abstract senes histograms of image gradients are also used in HOG and SIFt descriptors. 
# The visual equivalent of the NLP bag of words technique that search engines use is also a
# histogram. The reason that histograms are so useful is that the capture the frequency 
# distribution of a data set. These frequency distributions provide ways to build simple image
# processing techniques. 

# Content based image retrieval or image search engines are a great example of where histograms
# will be seen being used. You will be able to build a basic image search engine relying solely
# on the colour distribution of input images rather than using more advanced techniques like visual
# bag of words. For example if using a dataset of shirt images instead of labelling the images seperately
# and then using various deep learning techniques instead train to search for certain histograms. Histograms
# can then be compared and if similar such as when comparing pixels using various distance measurements such
# as Manhattan distance or Euclidean distance to see if the distance is small, if the distance is small then
# the shirts are likely to be of a similar colour.

# import the necessary packages
from matplotlib import pyplot as plt
import argparse
# Imutils contains the opencv2matplotlib function which handles displaying RGB versus BGR images with matplotlib
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["image"])

# split the image into its respective channels, then initialize the
# tuple of channel names along with our figure for plotting
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and plot it
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])

# create a new figure and then plot a 2D color histogram for the
# green and blue channels, using the word 'and' allows for constructing
# multidimensional histograms
fig = plt.figure()
ax = fig.add_subplot(131)
# Unlike single dimensional histograms where the examples have used 256 bins
# for demonstration purposes. This is not practical as it would for example result
# in histogram bins of over 65k were most applications use between 8 and 64. 
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32],
	[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

# plot a 2D color histogram for the green and red channels
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32],
	[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

# plot a 2D color histogram for blue and red channels
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32],
	[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

# finally, let's examine the dimensionality of one of the 2D
# histograms
print("2D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))

# our 2D histogram could only take into account 2 out of the 3
# channels in the image so now let's build a 3D color histogram
# (utilizing all channels) with 8 bins in each direction -- we
# can't plot the 3D histogram, but the theory is exactly like
# that of a 2D histogram, so we'll just show the shape of the
# histogram
hist = cv2.calcHist([image], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))

# display the original input image
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))

# show our plots
plt.show()
