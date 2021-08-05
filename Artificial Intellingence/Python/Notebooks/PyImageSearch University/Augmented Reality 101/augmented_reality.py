# import the necessary packages
import numpy as np
import cv2

# There is a text version of the tutorial available at the following address
# https://www.pyimagesearch.com/2021/01/11/opencv-video-augmented-reality/

# OpenCV is geared towards working with real-time image processing but can be
# used to facilitate real-time augmented reality. The purpose of the tutorial 
# is to access a data stream, detect any ArUco markers, then take an input image
# and apply a perspective transform to map the source input onto the frame

# Running this initially will have a lot of flickering, this is due to the ArUco
# tags not always being detected. This can be a problem due to having a low quality 
# frames have AR applied. There is however a fix available which is to 
# use reference point caching which is when the four ArUco markers are not detected 
# in the current frame, then fall back to their location in the previous frame where 
# all four were detected.

# initialize our cached reference points
# This is the location of ArUco tag markers in the previous frames
CACHED_REF_PTS = None

# This reuses logic from the opencv ar example as well as an slightly 
# changed augmented_reality file in the pyimagesearch folder
# Frame means webcam, source is from video file.
def find_and_warp(frame, source, cornerIDs, arucoDict, arucoParams,
	useCache=False):
	# grab a reference to our cached reference points
	global CACHED_REF_PTS

	# grab the width and height of the frame and source image,
	# respectively
	(imgH, imgW) = frame.shape[:2]
	(srcH, srcW) = source.shape[:2]

	# detect AruCo markers in the input frame
	(corners, ids, rejected) = cv2.aruco.detectMarkers(
		frame, arucoDict, parameters=arucoParams)

	# if we *did not* find our four ArUco markers, initialize an
	# empty IDs list, otherwise flatten the ID list
	ids = np.array([]) if len(corners) != 4 else ids.flatten()

	# initialize our list of reference points
	refPts = []

	# loop over the IDs of the ArUco markers in top-left, top-right,
	# bottom-right, and bottom-left order
	for i in cornerIDs:
		# grab the index of the corner with the current ID
		j = np.squeeze(np.where(ids == i))

		# if we receive an empty list instead of an integer index,
		# then we could not find the marker with the current ID
		if j.size == 0:
			continue

		# otherwise, append the corner (x, y)-coordinates to our list
		# of reference points
		corner = np.squeeze(corners[j])
		refPts.append(corner)

	# check to see if we failed to find the four ArUco markers
	if len(refPts) != 4:
		# if we are allowed to use cached reference points, fall
		# back on them
		if useCache and CACHED_REF_PTS is not None:
			refPts = CACHED_REF_PTS

		# otherwise, we cannot use the cache and/or there are no
		# previous cached reference points, so return early
		else:
			return None

	# if we are allowed to use cached reference points, then update
	# the cache with the current set
	if useCache:
		CACHED_REF_PTS = refPts

	# unpack our ArUco reference points and use the reference points
	# to define the *destination* transform matrix, making sure the
	# points are specified in top-left, top-right, bottom-right, and
	# bottom-left order
	(refPtTL, refPtTR, refPtBR, refPtBL) = refPts
	dstMat = [refPtTL[0], refPtTR[1], refPtBR[2], refPtBL[3]]
	dstMat = np.array(dstMat)

	# define the transform matrix for the *source* image in top-left,
	# top-right, bottom-right, and bottom-left order
	srcMat = np.array([[0, 0], [srcW, 0], [srcW, srcH], [0, srcH]])

	# compute the homography matrix and then warp the source image to
	# the destination based on the homography
	(H, _) = cv2.findHomography(srcMat, dstMat)
	warped = cv2.warpPerspective(source, H, (imgW, imgH))

	# construct a mask for the source image now that the perspective
	# warp has taken place (we'll need this mask to copy the source
	# image into the destination)
	mask = np.zeros((imgH, imgW), dtype="uint8")
	cv2.fillConvexPoly(mask, dstMat.astype("int32"), (255, 255, 255),
		cv2.LINE_AA)

	# this step is optional, but to give the source image a black
	# border surrounding it when applied to the source image, you
	# can apply a dilation operation
	rect = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
	mask = cv2.dilate(mask, rect, iterations=2)

	# create a three channel version of the mask by stacking it
	# depth-wise, such that we can copy the warped source image
	# into the input image
	maskScaled = mask.copy() / 255.0
	maskScaled = np.dstack([maskScaled] * 3)

	# copy the warped source image into the input image by
	# (1) multiplying the warped image and masked together,
	# (2) then multiplying the original input image with the
	# mask (giving more weight to the input where there
	# *ARE NOT* masked pixels), and (3) adding the resulting
	# multiplications together
	warpedMultiplied = cv2.multiply(warped.astype("float"),
		maskScaled)
	imageMultiplied = cv2.multiply(frame.astype(float),
		1.0 - maskScaled)
	output = cv2.add(warpedMultiplied, imageMultiplied)
	output = output.astype("uint8")

	# return the output frame to the calling function
	return output
