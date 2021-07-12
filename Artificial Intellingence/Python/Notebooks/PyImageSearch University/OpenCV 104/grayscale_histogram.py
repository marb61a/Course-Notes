# USAGE
# python grayscale_histogram.py --image beach.png

# This is the simplest type of histogram

# import the necessary packages
# matplotlib will be used for plotting histograms
from matplotlib import pyplot as plt
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute a grayscale histogram
# The first parameter is the image that is being processed.
# After that then there is a 0 passed in which tells calcHist that it is the
# zeroth channel which is just the grayscale image itself. This value would be 
# different if using an RGB image although bgr ordering would still apply.
# None is passed in because there is no mask present although if we had a mask
# we would pass it in so that a histogram could be computed for just the masked
# region. 256 is the number of bins being used in the histogram. The final 
# parameter being passed in is the range of possible pixel values. Once this function
# runs the histogram will be genereated, the x-axis will show the bins 0 - 256 and the
# y axis will show how often each of the different pixel intensities occurs.
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# matplotlib expects RGB images so convert and then display the image
# with matplotlib
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))

# plot the histogram
# Here we are showing raw pixel intensities of the image, for example if we have
# 256 * 256 pixel intensities this is a lot, if we resize to 32 * 32 then the image
# histogram is going to look a lot different but they should be similar due to the 
# contents being the same. This is why normalisation is used, we divide the histogram
# bins by the sum of the histogram values, all bin values when summed should add up to 1
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

# normalize the histogram
hist /= hist.sum()

# plot the normalized histogram
plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
