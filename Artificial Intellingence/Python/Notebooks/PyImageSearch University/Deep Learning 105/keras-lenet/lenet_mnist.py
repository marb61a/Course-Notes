# USAGE
# python lenet_mnist.py

# The text version of the tutorial is available at the following url
# https://www.pyimagesearch.com/2021/05/22/lenet-recognizing-handwritten-digits/

# The tutorial covers how to implement a lenet architecture using Keras and TensorFlow
# LeNet is a very popular architecture and is based on a 1988 paper which can be found at
# the following address https://ieeexplore.ieee.org/document/726791
# This can be thought of as being analogous to a Hello World program but in Deep Learning 
# and Computer Vision. The LeNet architecture is straightforward and small (in terms of 
# memory footprint), making it perfect for teaching the basics of CNNs. The tutorial will
# cover replicating the experiments from that paper.

# The LeNet architecture is a great real world network to learn for students because it is
# small enough to understand but can provide some interesting results. Using the LeNet network
# in conjunction with the MNIST database is fairly straightforward to run on most computers
# so that means beginners benefit. The architecture diagram from LeNet looks like the following
# INPUT => CONV => TANH => POOL => CONV => TANH => POOL => FC => TANH => FC. The LeNet architecture 
# uses the tanh activation function rather than the more popular ReLU. This is because ReLU had 
# not been used in the context of deep learning — it was more common to use tanh or sigmoid as an 
# activation function. However when using LeNet now then tanh is swapped out for ReLU

# There is a new file inside the pyimagesearch module --> lenet.py, this file stores the implementation
# of the LeNet architecture. This uses a sequential import which is just a directed graph. MaxPooling2D
# which is responsible for the pooling activities. Activation uses ReLU instead of Hyper Tangent. The build
# method accepts 4 parameters, width and height are both 28, depth is 1 and classes for the MNIST database
# will be 10.


# import the necessary packages
from pyimagesearch.nn.conv import LeNet
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.datasets import mnist
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from tensorflow.keras import backend as K
import matplotlib.pyplot as plt
import numpy as np

# grab the MNIST dataset (if this is your first time using this
# dataset then the 11MB download may take a minute)
print("[INFO] accessing MNIST...")
((trainData, trainLabels), (testData, testLabels)) = mnist.load_data()

# if we are using "channels first" ordering, then reshape the
# design matrix such that the matrix is:
# num_samples x depth x rows x columns
if K.image_data_format() == "channels_first":
	trainData = trainData.reshape((trainData.shape[0], 1, 28, 28))
	testData = testData.reshape((testData.shape[0], 1, 28, 28))

# otherwise, we are using "channels last" ordering, so the design
# matrix shape should be: num_samples x rows x columns x depth
else:
	trainData = trainData.reshape((trainData.shape[0], 28, 28, 1))
	testData = testData.reshape((testData.shape[0], 28, 28, 1))

# scale data to the range of [0, 1]
trainData = trainData.astype("float32") / 255.0
testData = testData.astype("float32") / 255.0

# convert the labels from integers to vectors
le = LabelBinarizer()
trainLabels = le.fit_transform(trainLabels)
testLabels = le.transform(testLabels)

# initialize the optimizer and model
print("[INFO] compiling model...")
opt = SGD(lr=0.01)
model = LeNet.build(width=28, height=28, depth=1, classes=10)
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# train the network
print("[INFO] training network...")
H = model.fit(trainData, trainLabels,
	validation_data=(testData, testLabels), batch_size=128,
	epochs=20, verbose=1)

# evaluate the network
print("[INFO] evaluating network...")
predictions = model.predict(testData, batch_size=128)
print(classification_report(testLabels.argmax(axis=1),
	predictions.argmax(axis=1),
	target_names=[str(x) for x in le.classes_]))

# plot the training loss and accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 20), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, 20), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, 20), H.history["accuracy"], label="train_acc")
plt.plot(np.arange(0, 20), H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()
