# USAGE
# python train_with_sequential_aug.py

# import the necessary packages
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers.experimental import preprocessing
import matplotlib.pyplot as plt
import tensorflow as tf
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--plot", type=str, default="training_plot.png",
	help="path to output training history plot")
args = vars(ap.parse_args())

# define training hyperparameters
BATCH_SIZE = 64
EPOCHS = 50

# load the CIFAR-10 dataset
print("[INFO] loading training data...")
((trainX, trainLabels), (textX, testLabels)) = cifar10.load_data()

# initialize our sequential data augmentation pipeline for training
trainAug = Sequential([
	preprocessing.Rescaling(scale=1.0 / 255),
	preprocessing.RandomFlip("horizontal_and_vertical"),
	preprocessing.RandomZoom(
		height_factor=(-0.05, -0.15),
		width_factor=(-0.05, -0.15)),
	preprocessing.RandomRotation(0.3)
])

# initialize a second data augmentation pipeline for testing (this
# one will only do pixel intensity rescaling
testAug = Sequential([
	preprocessing.Rescaling(scale=1.0 / 255)
])

# prepare the training data pipeline (notice how the augmentation
# layers have been mapped)
trainDS = tf.data.Dataset.from_tensor_slices((trainX, trainLabels))
trainDS = (
	trainDS
	.shuffle(BATCH_SIZE * 100)
	.batch(BATCH_SIZE)
	.map(lambda x, y: (trainAug(x), y),
		 num_parallel_calls=tf.data.AUTOTUNE)
	.prefetch(tf.data.AUTOTUNE)
)

# create our testing data pipeline (notice this time that we are
# *not* apply data augmentation)
testDS = tf.data.Dataset.from_tensor_slices((textX, testLabels))
testDS = (
	testDS
	.batch(BATCH_SIZE)
	.map(lambda x, y: (testAug(x), y),
		num_parallel_calls=tf.data.AUTOTUNE)
	.prefetch(tf.data.AUTOTUNE)
)

# initialize the model as a super basic CNN with only a single CONV
# and RELU layer, followed by a FC and soft-max classifier
print("[INFO] initializing model...")
model = Sequential()
model.add(Conv2D(32, (3, 3), padding="same",
	input_shape=(32, 32, 3)))
model.add(Activation("relu"))
model.add(Flatten())
model.add(Dense(10))
model.add(Activation("softmax"))

# compile the model
print("[INFO] compiling model...")
model.compile(loss="sparse_categorical_crossentropy",
	optimizer="sgd", metrics=["accuracy"])

# train the model
print("[INFO] training model...")
H = model.fit(
	trainDS,
	validation_data=testDS,
	epochs=EPOCHS)

# show the accuracy on the testing set
(loss, accuracy) = model.evaluate(testDS)
print("[INFO] accuracy: {:.2f}%".format(accuracy * 100))

# plot the training loss and accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(H.history["loss"], label="train_loss")
plt.plot(H.history["val_loss"], label="val_loss")
plt.plot(H.history["accuracy"], label="train_acc")
plt.plot(H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy on Dataset")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")
plt.savefig(args["plot"])