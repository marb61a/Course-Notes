# USAGE
# python match_histograms.py --source empire_state_cloudy.png --reference empire_state_sunset.png

# The text version of the tutorial is available at the following url
# https://www.pyimagesearch.com/2021/02/08/histogram-matching-with-opencv-scikit-image-and-python/

# What if you wanted to match the contrast or color distribution of two images automatically
# Histogram matching is beneficial when applying image processing pipelines to images captured 
# in different lighting conditions. This will create a normalised representation of images,
# regardless of the lighting conditions they were captured in.

# Histogram matching can best be thought of as a “transformation.”  The goal is to take an image
# and updated it's pixel intensities such that the distribution of the input image histogram 
# matches the distribution of a reference image. It is important to note that the image contents
# do not change but pixel distribution does.

# An example is when going to the beach during the day, if we want to have it during the sunset
# we can get a source image of a beach at sunset and apply the pixel intensities from this image
# on to the daytime image changing it to a sunset color images. Color correction cards are used by 
# image professionals and by using color matching techniques you can have a standard set of lighting
# across images. Applying histogram matching allows us to obtain interesting aesthetic results as well 
# as allowing us to create reliable image processing pipelines. 

# import the necessary packages
# Ensure sci-kit image is installed - https://scikit-image.org/
from skimage import exposure
import matplotlib.pyplot as plt
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True,
	help="path to the input source image")
ap.add_argument("-r", "--reference", required=True,
	help="path to the input reference image")
args = vars(ap.parse_args())

# load the source and reference images
print("[INFO] loading source and reference images...")
src = cv2.imread(args["source"])
ref = cv2.imread(args["reference"])

# determine if we are performing multichannel histogram matching
# and then perform histogram matching itself
print("[INFO] performing histogram matching...")
multi = True if src.shape[-1] > 1 else False
matched = exposure.match_histograms(src, ref, multichannel=multi)

# show the output images
cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)
cv2.waitKey(0)

# construct a figure to display the histogram plots for each channel
# before and after histogram matching was applied
(fig, axs) =  plt.subplots(nrows=3, ncols=3, figsize=(8, 8))

# loop over our source image, reference image, and output matched
# image
for (i, image) in enumerate((src, ref, matched)):
	# convert the image from BGR to RGB channel ordering
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# loop over the names of the channels in RGB order
	for (j, color) in enumerate(("red", "green", "blue")):
		# compute a histogram for the current channel and plot it
		(hist, bins) = exposure.histogram(image[..., j],
			source_range="dtype")
		axs[j, i].plot(bins, hist / hist.max())

		# compute the cumulative distribution function for the
		# current channel and plot it
		(cdf, bins) = exposure.cumulative_distribution(image[..., j])
		axs[j, i].plot(bins, cdf)

		# set the y-axis label of the current plot to be the name
		# of the current color channel
		axs[j, 0].set_ylabel(color)

# set the axes titles
axs[0, 0].set_title("Source")
axs[0, 1].set_title("Reference")
axs[0, 2].set_title("Matched")

# display the output plots
plt.tight_layout()
plt.show()