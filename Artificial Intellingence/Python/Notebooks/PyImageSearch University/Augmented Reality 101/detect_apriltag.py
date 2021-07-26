# USAGE
# python detect_apriltag.py --image images/example_01.png

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2020/11/02/apriltag-with-python/

# April tags are a type of Fiducial Marker which are reference objects that are
# placed in the field of view of a camera when a video or images is being captured.
# AprilTags are a specific type of fiducial marker, consisting of a black square with 
# a white foreground that has been generated in a particular pattern. The black border 
# surrounding the marker makes it easier for computer vision and image processing 
# algorithms to detect the AprilTags in a variety of scenarios.
# AprilTag can be thought of as conceptually similar to a QR code — a 2D binary pattern 
# that can be detected using computer vision algorithms, however AprilTags hold only 4 - 12
# bits of data whereas QR code holds upto 3kb of data. This is a feature and not a limititation
# but is a feature as these payloads are more easily detected and less difficult to detect at
# long ranges.  

# One AprilTag library is available at the following url -> https://april.eecs.umich.edu/software/apriltag 
# AprilTags and fiducial markers are used in many parts of computer vision systems such as
# Camera calibration, Measuring the distance between the camera and an object, Object size Estimation
# 3D Positioning. These tags can be created using basic software and a printer and Python libraries
# exist to automatically detect the tages for you.

# You will need to use Pip to install the  Python AprilTag library -> pip install apriltag
# This works with Python 2, 3 and OpenCV Images. OpenCV has its own implementation but has 
# difficulty with detecting some tags if partially obscured or occluded

# import the necessary packages
import apriltag
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image containing AprilTag")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
print("[INFO] loading image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# define the AprilTags detector options and then detect the AprilTags
# in the input image
print("[INFO] detecting AprilTags...")
# The family of tag will need to be specified as it will not be detected automatically.
# If unsure then some experimentation will be needed, tag36h11 is the standard family that 
# is used.
options = apriltag.DetectorOptions(families="tag36h11")
detector = apriltag.Detector(options)
results = detector.detect(gray)
print("[INFO] {} total AprilTags detected".format(len(results)))

# loop over the AprilTag detection results
for r in results:
	# extract the bounding box (x, y)-coordinates for the AprilTag
	# and convert each of the (x, y)-coordinate pairs to integers
	(ptA, ptB, ptC, ptD) = r.corners
	ptB = (int(ptB[0]), int(ptB[1]))
	ptC = (int(ptC[0]), int(ptC[1]))
	ptD = (int(ptD[0]), int(ptD[1]))
	ptA = (int(ptA[0]), int(ptA[1]))

	# draw the bounding box of the AprilTag detection
	cv2.line(image, ptA, ptB, (0, 255, 0), 2)
	cv2.line(image, ptB, ptC, (0, 255, 0), 2)
	cv2.line(image, ptC, ptD, (0, 255, 0), 2)
	cv2.line(image, ptD, ptA, (0, 255, 0), 2)

	# draw the center (x, y)-coordinates of the AprilTag
	(cX, cY) = (int(r.center[0]), int(r.center[1]))
	cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)

	# draw the tag family on the image
	tagFamily = r.tag_family.decode("utf-8")
	cv2.putText(image, tagFamily, (ptA[0], ptA[1] - 15),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
	print("[INFO] tag family: {}".format(tagFamily))

# show the output image after AprilTag detection
cv2.imshow("Image", image)
cv2.waitKey(0)