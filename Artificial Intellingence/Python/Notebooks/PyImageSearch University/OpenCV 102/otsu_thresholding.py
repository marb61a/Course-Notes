# USAGE
# python otsu_thresholding.py --image images/coins01.png

# This type of threshold removes the need to manually set a threshold flag
# we simply use a value of 0 and call the THRESH_OTSU flag
# Otsu assumes a bi-modal distribution of pixel intensities, bi-modal means
# that there are 2 peaks. When there are more than 2 peaks there can be an image
# with using Otsu which may have trouble with more than 2 peaks

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Image", image)

# convert the image to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# apply Otsu's automatic thresholding which automatically determines
# the best threshold value. 0 is essentially ignored once the THRESH_OTSU flag
# is called. There are 2 different values returned, T is the value automatically
# computed by Otsu for the test pixel
(T, threshInv) = cv2.threshold(blurred, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))

# visualize only the masked regions in the image
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)