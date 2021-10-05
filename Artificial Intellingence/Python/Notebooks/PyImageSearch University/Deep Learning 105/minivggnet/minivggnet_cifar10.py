# USAGE
# python minivggnet_cifar10.py --output output/cifar10_minivggnet_with_bn.png

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2021/05/22/minivggnet-going-deeper-with-cnns/

# VGGNet was first introduced in a 2014 paper which can be found the following address
# https://arxiv.org/abs/1409.1556
# This paper showed that having an architecture with very small (3×3) filters can still
# be trained to increasingly higher depths (16-19 layers) and obtain state-of-the-art 
# classification on the challenging ImageNet classification challenge. This is very
# popular in the deep learning community as it shows what CNN's are capable of achieving
# Some of the datasets and gpus were not as capable which meant that some things that were
# being shown by LeNet were not being digested properly. Other factors such as mixed filter
# sizes being used in network architectures were prevalent, the first layer of a network
# for example was usuallt between 7x7 and 11x11, it was only the deepest network layers that
# used a 3x3 size. 

# This is where VGGNet is unique in that it uses 3×3 kernels throughout the entire architecture.
# The use of these small kernels is arguably what helps VGGNet generalize to classification 
# problems outside where the network was originally trained. Anytime that a 3x3 network can be
# seen it is a fair bet that it was inspired by VGGNet, there are 16 and 19 layer variants of
# VGGNet but that is for a more advanced level.

# set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")

# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from pyimagesearch.nn.conv import MiniVGGNet
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

# load the training and testing data, then scale it into the
# range [0, 1]
print("[INFO] loading CIFAR-10 data...")
((trainX, trainY), (testX, testY)) = cifar10.load_data()
trainX = trainX.astype("float") / 255.0
testX = testX.astype("float") / 255.0

# convert the labels from integers to vectors
lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)

# initialize the label names for the CIFAR-10 dataset
labelNames = ["airplane", "automobile", "bird", "cat", "deer",
	"dog", "frog", "horse", "ship", "truck"]

# initialize the optimizer and model
print("[INFO] compiling model...")
opt = SGD(lr=0.01, decay=0.01 / 40, momentum=0.9, nesterov=True)
model = MiniVGGNet.build(width=32, height=32, depth=3, classes=10)
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# train the network
print("[INFO] training network...")
H = model.fit(trainX, trainY, validation_data=(testX, testY),
	batch_size=64, epochs=40, verbose=1)

# evaluate the network
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=64)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1), target_names=labelNames))

# plot the training loss and accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 40), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, 40), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, 40), H.history["accuracy"], label="train_acc")
plt.plot(np.arange(0, 40), H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy on CIFAR-10")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig(args["output"])
