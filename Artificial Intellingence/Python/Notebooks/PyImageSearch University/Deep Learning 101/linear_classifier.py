# USAGE
# python linear_classifier.py --dataset kaggle_dogs_vs_cats

# A link which relates to the following tutorial -> Stamford Linear Classification Notes
# https://cs231n.github.io/linear-classify/

# There is a text version of the tutorial available at the following address
# https://www.pyimagesearch.com/2016/08/22/an-intro-to-linear-classification-with-python/

# In the context of deep learning the most prohibitive aspect of k-NN is the data itself
# While training may be simple, testing is quite slow, with the bottleneck being the distance 
# computation between vectors. There are things that can be done to speed up the searching such
# as Approximate Nearest Neighbor with methods like  ANN, FLANN, or Annoy.

# There is a better approach which can be used. This type of machine learning is called parameterized
# learning, this is where define a machine learning model that can learn patterns from our input data 
# during training time but have the benefit of being defined by a small number of parameters which
# represent a model irrespective of training size. The model will always be the same size regardless
# of how much training data is used

# Paramaterisation may seem difficult but is simply the process of defining the necessary parameters 
# of a given model. There are 4 components which are used in parameterised learning. Firstly is Data
# which can be class labels, pixel intensities etc. The second component is the scoring function which
# takes in the input images, performs functionality on them and returns output predictions. Then there is
# the loss function which measures the agreement between predicted class labels and ground truth class
# labels, basically it will tell how good and accurate the predictions being made are. Then there are the
# parameters which are the weights and biases and these are updated during the process

# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import os


def extract_color_histogram(image, bins=(8, 8, 8)):
	# extract a 3D color histogram from the HSV color space using
	# the supplied number of `bins` per channel
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	hist = cv2.calcHist([hsv], [0, 1, 2], None, bins,
		[0, 180, 0, 256, 0, 256])

	# handle normalizing the histogram if we are using OpenCV 2.4.X
	if imutils.is_cv2():
		hist = cv2.normalize(hist)

	# otherwise, perform "in place" normalization in OpenCV 3
	else:
		cv2.normalize(hist, hist)

	# return the flattened histogram as the feature vector
	return hist.flatten()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
args = vars(ap.parse_args())

# grab the list of images that we'll be describing
print("[INFO] describing images...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialize the data matrix and labels list
data = []
labels = []

# loop over the input images
for (i, imagePath) in enumerate(imagePaths):
	# load the image and extract the class label (assuming that our
	# path as the format: /path/to/dataset/{class}.{image_num}.jpg
	image = cv2.imread(imagePath)
	label = imagePath.split(os.path.sep)[-1].split(".")[0]

	# extract a color histogram from the image, then update the
	# data matrix and labels list
	hist = extract_color_histogram(image)
	data.append(hist)
	labels.append(label)

	# show an update every 1,000 images
	if i > 0 and i % 1000 == 0:
		print("[INFO] processed {}/{}".format(i, len(imagePaths)))

# encode the labels, converting them from strings to integers
le = LabelEncoder()
labels = le.fit_transform(labels)

# partition the data into training and testing splits, using 75%
# of the data for training and the remaining 25% for testing
print("[INFO] constructing training/testing split...")
(trainData, testData, trainLabels, testLabels) = train_test_split(
	np.array(data), labels, test_size=0.25, random_state=42)

# train the linear regression clasifier
print("[INFO] training Linear SVM classifier...")
model = LinearSVC()
model.fit(trainData, trainLabels)

# evaluate the classifier
print("[INFO] evaluating classifier...")
predictions = model.predict(testData)
print(classification_report(testLabels, predictions,
	target_names=le.classes_))
