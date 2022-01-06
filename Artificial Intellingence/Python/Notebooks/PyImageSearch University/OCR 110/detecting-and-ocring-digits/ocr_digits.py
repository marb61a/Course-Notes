# USAGE
# python ocr_digits.py --image apple_support.png
# python ocr_digits.py --image apple_support.png --digits 0

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2021/08/30/detecting-and-ocring-digits-with-tesseract-and-python/

# The tutorial will cover how to detect and then ocr digits. There are a few different use cases
# where getting digits from an image is needed eg getting a phone number from a business card
# or getting figures from an invoice

# import the necessary packages
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")

# The digits argument is added as if it is greater than 0 then only digits will be gotten from
# the image, less than 0 means all parts of the image will be fetched by the ocr engine
ap.add_argument("-d", "--digits", type=int, default=1,
	help="whether or not *digits only* OCR will be performed")
args = vars(ap.parse_args())

# load the input image, convert it from BGR to RGB channel ordering,
# and initialize our Tesseract OCR options as an empty string
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

# check to see if *digit only* OCR should be performed, and if so,
# update our Tesseract OCR options
if args["digits"] > 0:
	options = "outputbase digits"

# OCR the input image using Tesseract
text = pytesseract.image_to_string(rgb, config=options)
print(text)
