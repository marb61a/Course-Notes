# USAGE
# python whitelist_blacklist.py --image pa_license_plate.png
# python whitelist_blacklist.py --image pa_license_plate.png --blacklist "*#"
# python whitelist_blacklist.py --image invoice.png --whitelist "0123456789$.-"
# python whitelist_blacklist.py --image invoice.png --whitelist "0123456789.-" --blacklist "0"

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2021/09/06/whitelisting-and-blacklisting-characters-with-tesseract-and-python/

# Using tesseract to blacklist or whitelist characters to filter what characters are being gotten when running
# the ocr ending on an image. This is similar to using whitelisting or blacklisting concepts used elsewhere.
# Sometimes when characters are blacklisted they are not eliminated but replaced so the replacement character
# will also have to be removed. Balcklists and whitelists can be applied simultaneously

# import the necessary packages
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")

# This is the list of characters that will be allowed
ap.add_argument("-w", "--whitelist", type=str, default="",
	help="list of characters to whitelist")

# This is the list of characters that will not be allowed
ap.add_argument("-b", "--blacklist", type=str, default="",
	help="list of characters to blacklist")
args = vars(ap.parse_args())

# load the input image, swap channel ordering, and initialize our
# Tesseract OCR options as an empty string
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

# check to see if a set of whitelist characters has been provided,
# and if so, update our options string
if len(args["whitelist"]) > 0:
	options += "-c tessedit_char_whitelist={} ".format(
		args["whitelist"])

# check to see if a set of blacklist characters has been provided,
# and if so, update our options string
if len(args["blacklist"]) > 0:
	options += "-c tessedit_char_blacklist={}".format(
		args["blacklist"])

# OCR the input image using Tesseract
text = pytesseract.image_to_string(rgb, config=options)
print(text)
