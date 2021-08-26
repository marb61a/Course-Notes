# USAGE
# python keras_cifar10.py --output output/keras_cifar10.png

# There is a text version of the tutorial vailable at the following address
# https://www.pyimagesearch.com/2021/05/06/implementing-feedforward-neural-networks-with-keras-and-tensorflow/

# This tutorial will show how to implement Feedfoward Perceptrons using both the Keras and Tensorflow libraries
# Keras --> https://keras.io/
# Tensorflow --> https://www.tensorflow.org/
# The example datasets being used are the MNIST and CIFAR-10 datasets. The purpose of the tutorial is not to
# build hi-tech state of the art NN but to implement simple neural networks using the Keras library. This example
# will be resued in later courses when comparing to Convolutional Neural Networks which will outperform what we
# have learned so far quite easily.

# This example uses the full MNIST dataset consisting of 70,000 data points (7,000 examples per digit), Each data 
# point is represented by a 784-d vector, corresponding to the (flattened) 28×28 images in the MNIST dataset. This
# is because we cannot use nulti-dimensional images when training the model so flatten to a single dimension. The
# goal of the lesson is to get 90% accuracy on the dataset. Using Keras to build our network architecture is 
# substantially easier than our pure Python version, in this example the network architecture will only occupy four
# lines of code, the rest of the code is for loading data, labelling and displaying results.

# This (CIFAR) dataset differs from the MNIST dataset as the images are RGB, there are 10 different classes and the
# goals is to predict which class an image belongs to

# import the necessary packages
# LabelBinarizer is used for OneHotEncoding, it encodes integer labels as vector labels
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
# The Sequential API is designed to buil model architectures
from tensorflow.keras.models import Sequential
# Dense refers to full connected layers which as seen previously connects all nodes in a layer to every node in the
# next layer
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt
import numpy as np
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to the output loss/accuracy plot")
args = vars(ap.parse_args())

# load the training and testing data, scale it into the range [0, 1],
# then reshape the design matrix
print("[INFO] loading CIFAR-10 data...")
((trainX, trainY), (testX, testY)) = cifar10.load_data()
trainX = trainX.astype("float") / 255.0
testX = testX.astype("float") / 255.0
trainX = trainX.reshape((trainX.shape[0], 3072))
testX = testX.reshape((testX.shape[0], 3072))

# convert the labels from integers to vectors
lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)

# initialize the label names for the CIFAR-10 dataset
labelNames = ["airplane", "automobile", "bird", "cat", "deer",
	"dog", "frog", "horse", "ship", "truck"]

# define the 3072-1024-512-10 architecture using Keras
model = Sequential()
model.add(Dense(1024, input_shape=(3072,), activation="relu"))
model.add(Dense(512, activation="relu"))
model.add(Dense(10, activation="softmax"))

# train the model using SGD
# These are the only lines that are really needed to train an NN using Keras
print("[INFO] training network...")
sgd = SGD(0.01)
model.compile(loss="categorical_crossentropy", optimizer=sgd,
	metrics=["accuracy"])
H = model.fit(trainX, trainY, validation_data=(testX, testY),
	epochs=100, batch_size=32)

# evaluate the network
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1), target_names=labelNames))

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
plt.savefig(args["output"])
