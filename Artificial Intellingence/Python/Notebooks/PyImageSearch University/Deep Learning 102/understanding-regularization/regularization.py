# USAGE
# python regularization.py --dataset kaggle_dogs_vs_cats

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2016/09/19/understanding-regularization-for-image-classification-and-machine-learning/

# Again it is recommended that students study the text article prior to taking the video tutorial
# Regularisation is the ability of a model to generalise. While a loss function  in Gradient Descent
# allows for determining how well or bad a set of parameters are performing it does not take into
# account how a weight matrix looks. 

# When talking about looks we must keep in mind that there are an infinite set of parameters available 
# that will get a reasonable level of accuracy from a dataset. There needs to be an insurance that
# the model performs generalisation well which is were regularisation comes in and is the second most
# important hyperparameter to tune after learning rate.

# There are various different types of regularisation techniques such as L1, L2 or as it is also known 
# Weight Decay and Elastic Net. There are also types of regularisation that can be explicitly added to 
# the network architecture such as dropout as well as implicit form such as data augmentation. 

# Regualrisation helps with controlling a model capacity which ensures that models are better at making 
# (correct) classifications on data points that they were not trained on. Too much regualrisation can 
# also be an issue due to underfitting.

# Taking a cross-entropy loss function as an example, we are looking to improve W which is the weight matrix. 
# Specifically looking to improve the ability to generalise. The answer in this case is to define what
# is called a regularisation penalty which is a function that would operat on the weight matrix. This would
# have the effect of discouraging large weights in the function as this may lead to overfitting. 
# Regularisation may affect training accuracy negatively but will improve testing accuracy. The λ variable 
# is a hyperparameter that controls the amount or strength of the regularization to be applied.

# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import SGDClassifier
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

	# otherwise, perform "in place" normalization in OpenCV 3 (I
	# personally hate the way this is done
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

# loop over our set of regularizers
for r in (None, "l1", "l2", "elasticnet"):
	# train a Stochastic Gradient Descent classifier using a softmax
	# loss function, the specified regularizer, and 10 epochs
	print("[INFO] training model with `{}` penalty".format(r))
	model = SGDClassifier(loss="log", penalty=r, random_state=967,
		n_iter=10)
	model.fit(trainData, trainLabels)

	# evaluate the classifier
	acc = model.score(testData, testLabels)
	print("[INFO] `{}` penalty accuracy: {:.2f}%".format(r, acc * 100))