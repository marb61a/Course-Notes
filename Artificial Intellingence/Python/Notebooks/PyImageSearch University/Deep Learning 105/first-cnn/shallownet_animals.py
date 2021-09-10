# USAGE
# python shallownet_animals.py --dataset ../datasets/animals

# There is a text version of the tutorial available at the following address
# https://www.pyimagesearch.com/2021/05/22/a-gentle-guide-to-training-your-first-cnn-with-keras-and-tensorflow/

# The animals dataset being used is also available from the following url (180mb download)
# https://pis-datasets.s3.us-east-2.amazonaws.com/animals.zip
# There are approximately 3000 image files in the dataset, in 3 folders, Cats, Dogs and Panda

# This will be the first tutorial learning how to train a Neural Network using Keras and Tensorflow
# This file along with the cifar10 file will allow for loading the dataset and then training a Neural Network 
# on that set. The goal is to train the network so that it can correctly identify which class an image belongs to.

# The pyimagesearch module has grown too, there is a NN folder which holds a CONV folder and that in turn holds the
# shallownet.py file. This is a basic CNN consisting of a single convolutional layer but the goal is to just to gain
# exposure to using Keras and Tensorflow. The preprocessing folder also has some new material namely the new
# imagetoarrayperprocessor.py file which takes an image loaded by OpenCV2 which is represented by a numpy array and 
# then convert it to a format compatible with Keras and TF. 

# It might be a good idea to have a class/folder which holds any network architectures that are to be implemented as
# it will keep the environment clean on the computer and makes keeping track of files much easier.

# The simplepreprocessor that has been used for a while is chained to the new imagepreprocessor.py file, in the file
# the first thing that is done is to import the img_to_array function from TF. This function correctly orders channel
# dimensions on images that have been loaded and converted to numpy arrays. Keras can work with images of different
# formats, other libraries think of images in terms of channels, height and width, the channels are first and that is
# called channels first ordering whereas pytorch uses channel last ordering. This file ensures that the ordering is
# correct as there maybe cases where different ordering is used eg Keras is using a different backend than TensorFlow.
# The preprocess function is where different types of format can be set, it will be set usually to none in the file
# constructor.

# In the shallownet.py file there are multiple imports, sequential builds a simple directed graph from NN input to 
# output. The Conv2D class will be seen a lot of the time and is used to implement 2D convolution as this is where
# filters are specified. Activation is where the activation function comes from, the Flatten class takes output and
# flattens it down to a single dimension. This is used by the next import which is Dense and is used by fully
# connected layers. The backend in then imported which allows for checking if channels first or last is being used.
# In the build method there a 4 parameters, depth is the number of channels, 1 if Grayscale and 3 if RGB and the classes
# parameter is the total number of classes that are being learned. In the animals dataset there are 3 different classes
# so the parameter would be set to 3. The inputShape variable will have height, width and depth passed in that order as
# this is using channels last ordering and depth refers to channels. If using channels first then the depth would be
# passed in ahead of width and height. There is only 1 layer, in this case it will be with 32 filter each will be 3x3,
# padding is set to same which means output shape will be the same as input shape. Setting padding to valid which is the
# default will reduce the spacial dimensions of the input image. InputShape dimensions are declared as this is the only 
# layer in the network. The architecture can be described as INPUT => CONV => RELU => FC

# Training the model should be very quick as there is a small dataset and only a single layer, the plot generated shows
# a lot of signs of overfitting which is not good in training and there are techniques to put in place to avoid having
# overfitting. Using the shallownet_animals file for training there is a divergence around the epoch30 mark by the time
# that epoch 60 comes around there is saturation in the testing accuracy which leaves us unable to get more than 70%
# classification accuracy which again is due to overfitting and can only be solved by using techniques such as getting
# more data or augmenting the existing data.

# The cifar10.py file deals with the cifar10 dataset, this dataset can be brought in using the imports at the top of the
# file from TF. The 10 class labels are bought in, each image in cifar10 is only 32x32 pixels in size which is fairly
# small. This will take a while to train as there are more images to train in the cifar10 dataset, again there are signs
# of overfitting in validation loss. Training loss and validation loss should curve fairly similar when looking at them
# on the generated plot. It is also notoriously easy to overfit on the CIFAR-10 dataset due to the limited number of 
# low-resolution training samples


# import the necessary packages
# responsible for one hot encoding
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
# Importing files from the pyimagesearch module
from pyimagesearch.preprocessing import ImageToArrayPreprocessor
from pyimagesearch.preprocessing import SimplePreprocessor
from pyimagesearch.datasets import SimpleDatasetLoader
from pyimagesearch.nn.conv import ShallowNet
from tensorflow.keras.optimizers import SGD
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
args = vars(ap.parse_args())

# grab the list of images that we'll be describing
# this just gets the paths to the image, it does not load the image at all!!
print("[INFO] loading images...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialize the image preprocessors
# Each image will be resized to 32x32 pixels
sp = SimplePreprocessor(32, 32)
iap = ImageToArrayPreprocessor()

# load the dataset from disk then scale the raw pixel intensities
# to the range [0, 1]
sdl = SimpleDatasetLoader(preprocessors=[sp, iap])
(data, labels) = sdl.load(imagePaths, verbose=500)
data = data.astype("float") / 255.0

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.25, random_state=42)

# convert the labels from integers to vectors
trainY = LabelBinarizer().fit_transform(trainY)
testY = LabelBinarizer().fit_transform(testY)

# initialize the optimizer and model
print("[INFO] compiling model...")
opt = SGD(lr=0.005)
model = ShallowNet.build(width=32, height=32, depth=3, classes=3)
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# train the network
print("[INFO] training network...")
H = model.fit(trainX, trainY, validation_data=(testX, testY),
	batch_size=32, epochs=100, verbose=1)

# evaluate the network
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1),
	target_names=["cat", "dog", "panda"]))

# plot the training loss and accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 100), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, 100), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, 100), H.history["accuracy"], label="train_acc")
plt.plot(np.arange(0, 100), H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()
