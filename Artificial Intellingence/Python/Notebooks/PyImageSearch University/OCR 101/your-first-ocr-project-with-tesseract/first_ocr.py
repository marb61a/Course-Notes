# USAGE
# python first_ocr.py --image pyimagesearch_address.png
# python first_ocr.py --image steve_jobs.png

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2021/08/23/your-first-ocr-project-with-tesseract-and-python/

# The goal of the tutorial is to show how to OCR an image using Tesseract
# There are 3 different images available in the folder, one of the images has faded a little
# and may need a little help for text to be seen accurately

# Tesseract assumes that images being input are in RGB format so that will need to be fixed
# using OpenCV. Tesseract will also do some of the image preprocesssing and thresholding but
# only to a basic level. On many images there will be a need to make use of more advanced
# settings Tesseract is capable of. There is a need to really understand what is going on behind
# the scenes in order to make Tesseract much better.

# import the necessary packages
# pytesseract has numerous functions and communicates with Tesseract
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = vars(ap.parse_args())

# load the input image and convert it from BGR to RGB channel
# ordering
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use Tesseract to OCR the image
text = pytesseract.image_to_string(image)
print(text)
