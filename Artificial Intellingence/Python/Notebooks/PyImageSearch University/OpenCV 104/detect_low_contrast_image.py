# USAGE
# python detect_low_contrast_image.py --input examples2

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2021/01/25/detecting-low-contrast-images-with-opencv-scikit-image-and-python/

# The tutorial will be discussing a very specific application of image histograms.
# It is important to remember that it is orders of magnitude easier to write code for
# images captured in ideal lighting conditions than it is to write code for images
# captured in all kinds of different conditions. Where possible try and control conditions
# so the there is not the huge amount of work and experimentation that is needed to deal
# with images with differing lighting, contrast etc. Parameters can be hardcoded in ideal conditions
# whereas there may need to be dynamic parameters for non-ideal conditions which can be very complex.

# Again reusing the color card for the example but with reduced light and perfect light. The reduced
# light image is of much lesser quality. The example will also use the canny edge detector which needs
# certain parameters hardcoded. Edge detection will not work properly on the lower contrast image.

# scikit-image has the is_low_contrast function for when we are dealing with low contrast images. 
# https://scikit-image.org/docs/dev/api/skimage.exposure.html#skimage.exposure.is_low_contrast
# This is used to check if there are low contrast images being used. If there are low contrast images 
# detected then they are thrown out.

# import the necessary packages
from skimage.exposure import is_low_contrast
# Finds image in the cli specified directory
from imutils.paths import list_images
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input directory of images")
# In this case 0.35 is the fraction threshold for low contrast detection. As the official documentation
# states, an image is considered low- contrast when its range of brightness spans less than this fraction
# of its data type’s full range. This is the most important parameter and can be adjusted as needed. The 
# default is 0.05 and basically states that if 5% or less of pixel intensities spanning the 0 - 255 range
# then the image can be considered as being low contrast. 0.35 is a reasonably successful value but each
# image set should be experimented with using different values starting with default.
ap.add_argument("-t", "--thresh", type=float, default=0.35,
	help="threshold for low contrast")
args = vars(ap.parse_args())

# grab the paths to the input images
imagePaths = sorted(list(list_images(args["input"])))

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	# load the input image from disk, resize it, and convert it to
	# grayscale
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=450)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# blur the image slightly and perform edge detection
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(blurred, 30, 150)

	# initialize the text and color to indicate that the input image
	# is *not* low contrast
	text = "Low contrast: No"
	color = (0, 255, 0)

	# check to see if the image is low contrast
	if is_low_contrast(gray, fraction_threshold=args["thresh"]):
		# update the text and color
		text = "Low contrast: Yes"
		color = (0, 0, 255)

	# otherwise, the image is *not* low contrast, so we can continue
	# processing it
	else:
		# find contours in the edge map and find the largest one,
		# which we'll assume is the outline of our color correction
		# card
		cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		c = max(cnts, key=cv2.contourArea)

		# draw the largest contour on the image
		cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

	# draw the text on the output image
	cv2.putText(image, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
		color, 2)

	# show the output image and edge map
	cv2.imshow("Image", image)
	cv2.imshow("Edge", edged)
	cv2.waitKey(0)