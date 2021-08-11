# USAGE
# python knn.py --dataset dataset/animals

# The text version of the tutorial is available at the following url
# https://www.pyimagesearch.com/2021/04/17/your-first-image-classifier-using-k-nn-to-classify-images/

# The dataset used is not uploaded, it is simply a collection of animal images divided into folders
# which each contain a specific type i.e. Cats, Dogs and Pandas and can be put together anywhere.

# KNN can be considered as the simplest ML algorithm, this is because it does not do any learning
# It accepts in training data and instead of trying to learn patterns in the data it calculates
# the distance between them in an n-dimensional space. This is is still an important algorithm to review 
# so we can appreciate how neural networks learn from data in future lessons. KNN is not an intelligent
# algorithm but is still important to learn. 

# One of the biggest downsides of KNN is that in order to save the model to disk every image in the 
# training set must be saved to in order to make future predicitons. This has a huge inflationary
# impact on the model size. KNN is also fairly computationally expensive and is not particularly efficient
# when using memory.

# In the pyimagesearch module there is a pre-processing sub-module which conatins a simple 
# pre-processor which takes an image from disk and resizes it. The dataset sub-module which contains a
# simple dataset loader. Using these modules eliminates a lot of the data loading work from files and
# encapsulates. knn.py is the KNN driver script.

# The main reason for using a pre-processor and resizing images is that in order for KNN to work at all
# when computing distance, each vector must have the same dimensionality. KNN cannot compute Euclidean
# distance when there are differing dimensionalities.

# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from pyimagesearch.preprocessing import SimplePreprocessor
from pyimagesearch.datasets import SimpleDatasetLoader
from imutils import paths
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
ap.add_argument("-k", "--neighbors", type=int, default=1,
	help="# of nearest neighbors for classification")
ap.add_argument("-j", "--jobs", type=int, default=-1,
	help="# of jobs for k-NN distance (-1 uses all available cores)")
args = vars(ap.parse_args())

# grab the list of images that we'll be describing
print("[INFO] loading images...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialize the image preprocessor, load the dataset from disk,
# and reshape the data matrix
sp = SimplePreprocessor(32, 32)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels) = sdl.load(imagePaths, verbose=500)
data = data.reshape((data.shape[0], 3072))

# show some information on memory consumption of the images
print("[INFO] features matrix: {:.1f}MB".format(
	data.nbytes / (1024 * 1024.0)))

# encode the labels as integers
le = LabelEncoder()
labels = le.fit_transform(labels)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.25, random_state=42)

# train and evaluate a k-NN classifier on the raw pixel intensities
print("[INFO] evaluating k-NN classifier...")
model = KNeighborsClassifier(n_neighbors=args["neighbors"],
	n_jobs=args["jobs"])
model.fit(trainX, trainY)
print(classification_report(testY, model.predict(testX),
	target_names=le.classes_))
