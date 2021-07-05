# USAGE
# python basic_connected_components.py --image license_plate.png

# There is a text version of the tutorial available at the following address
# https://www.pyimagesearch.com/2021/02/22/opencv-connected-component-labeling-and-analysis/
# !!! This text tutorial should be read prior to looking at the video tutorial as there are
# additional explanations for some things compared to the video

# Connected Component Analysis is similar to cpntour extraction and detection but provides
# an extra step. This extra step examines how pixels are connected to each other in an image.
# More specifically a binary input image. Connected Component Analysis is also known as 
# Connected Component Labeeling, Blob Extraction or region labelling. It is an algorithmic
# application of graph theory and it can be used to determin the connectivity of blob like regions
# in a binary image.

# If we take a licence plate for an example,  we may want to look at extracting the various 
# letters and numbers, this can be done with contour detection and extraction but will not 
# tell us anything about how the components are connected. With connected component labelling 
# and analysis this can be done. Connected Component Analysis is another great technique to learn
# when learning OpenCV

# There are 4 different functions supplied by OpenCV for Connected Component Analysis. These are
# cv2.connectedComponents, cv2.connectedComponentsWithStats, cv2.connectedComponentsWithAlgorithm
# cv2.connectedComponentsWithStatsWithAlgorithm with cv2.connectedComponentsWithStats being the most 
# popular. 

# cv2.connectedComponentsWithStats returns different information such as The bounding box of the connected component
# The area of the component in pixels and the centre x, y coordinates of the component. cv2.connectedComponents
# is very similar to cv2.connectedComponentsWithStats but does not return stats information which is the majority
# of situations will be needed.  

# cv2.connectedComponentsWithAlgorithm, implements faster, more efficient algorithms for connected component analysis,
# if OpenCv is compiled with parallel processing then cv2.connectedComponentsWithAlgorithm and its version with stats
# will run faster that the other two algorithms.

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")

# For more information about the differences in connectivity options
# https://stackoverflow.com/questions/7088678/4-connected-vs-8-connected-in-connected-component-labeling-what-is-are-the-meri
ap.add_argument("-c", "--connectivity", type=int, default=4,
	help="connectivity for connected component analysis")
args = vars(ap.parse_args())

# load the input image from disk, convert it to grayscale, and
# threshold it. In this case it is the Otsu thresholding that is applied
# https://en.wikipedia.org/wiki/Otsu%27s_method
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Apply connected component analysis to the thresholded image
# There are 3 arguments passed in to the file, firstly is the binary thresh image,
# the second is the --connectivity command line argument and the final argument is the data
# type which should be left as is. This then returns 4 items, total number of unique labels that were
# detected, A mask named labels has the same spatial dimensions as our input thresh image, each location in 
# labels has an integer ID value which corresponds to the connected component where the pixel belongs.
# The statistics on each connected component, including the bounding box values and area in pixels and finally
# Centroids which are the cente x, y coordinates of each connected component
output = cv2.connectedComponentsWithStats(
	# The data type value is 32 bit short
	thresh, args["connectivity"], cv2.CV_32S)
(numLabels, labels, stats, centroids) = output

# loop over the number of unique connected component labels
for i in range(0, numLabels):
	# The first connected component, with an ID of 0, is always the background
	# *background* (typically we would just ignore this) however on occasion we may need it
	# so remember  ID 0 holds the background
	if i == 0:
		text = "examining component {}/{} (background)".format(
			i + 1, numLabels)

	# otherwise, we are examining an actual connected component
	else:
		text = "examining component {}/{}".format( i + 1, numLabels)

	# print a status message update for the current connected
	# component
	print("[INFO] {}".format(text))

	# extract the connected component statistics and centroid for
	# the current label
	x = stats[i, cv2.CC_STAT_LEFT]
	y = stats[i, cv2.CC_STAT_TOP]
	w = stats[i, cv2.CC_STAT_WIDTH]
	h = stats[i, cv2.CC_STAT_HEIGHT]
	area = stats[i, cv2.CC_STAT_AREA]
	(cX, cY) = centroids[i]

	# clone our original image (so we can draw on it) and then draw
	# a bounding box surrounding the connected component along with
	# a circle corresponding to the centroid
	output = image.copy()
	cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 3)
	cv2.circle(output, (int(cX), int(cY)), 4, (0, 0, 255), -1)

	# construct a mask for the current connected component by
	# finding a pixels in the labels array that have the current
	# connected component ID
	componentMask = (labels == i).astype("uint8") * 255

	# show our output image and connected component mask
	cv2.imshow("Output", output)
	cv2.imshow("Connected Component", componentMask)
	cv2.waitKey(0)
