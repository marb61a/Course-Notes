# USAGE
# python train_model.py

# set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")

# import the necessary packages
from pyimagesearch.cancernet import CancerNet
from pyimagesearch import config
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adagrad
from tensorflow.keras.utils import to_categorical
from tensorflow.data import AUTOTUNE
from imutils import paths
import matplotlib.pyplot as plt
import tensorflow as tf
import argparse
import os

def load_images(imagePath):
	# read the image from disk, decode it, convert the data type to
	# floating point, and resize it
	image = tf.io.read_file(imagePath)
	image = tf.image.decode_png(image, channels=3)
	image = tf.image.convert_image_dtype(image, dtype=tf.float32)
	image = tf.image.resize(image, config.IMAGE_SIZE)

	# parse the class label from the file path
	label = tf.strings.split(imagePath, os.path.sep)[-2]
	label = tf.strings.to_number(label, tf.int32)
	
	# return the image and the label
	return (image, label)

@tf.function
def augment(image, label):
	# perform random horizontal and vertical flips
	image = tf.image.random_flip_up_down(image)
	image = tf.image.random_flip_left_right(image)

	# return the image and the label
	return (image, label)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path to output loss/accuracy plot")
args = vars(ap.parse_args())

# grab all the training, validation, and testing dataset image paths
trainPaths = list(paths.list_images(config.TRAIN_PATH))
valPaths = list(paths.list_images(config.VAL_PATH))
testPaths = list(paths.list_images(config.TEST_PATH))

# calculate the total number of training images in each class and
# initialize a dictionary to store the class weights
trainLabels = [int(p.split(os.path.sep)[-2]) for p in trainPaths]
trainLabels = to_categorical(trainLabels)
classTotals = trainLabels.sum(axis=0)
classWeight = {}

# loop over all classes and calculate the class weight
for i in range(0, len(classTotals)):
	classWeight[i] = classTotals.max() / classTotals[i]

# build the training dataset and data input pipeline
trainDS = tf.data.Dataset.from_tensor_slices(trainPaths)
trainDS = (trainDS
	.shuffle(len(trainPaths))
	.map(load_images, num_parallel_calls=AUTOTUNE)
	.map(augment, num_parallel_calls=AUTOTUNE)
	.cache()
	.batch(config.BS)
	.prefetch(AUTOTUNE)
)

# build the validation dataset and data input pipeline
valDS = tf.data.Dataset.from_tensor_slices(valPaths)
valDS = (valDS
	.map(load_images, num_parallel_calls=AUTOTUNE)
	.cache()
	.batch(config.BS)
	.prefetch(AUTOTUNE)
)

# build the testing dataset and data input pipeline
testDS = tf.data.Dataset.from_tensor_slices(testPaths)
testDS = (testDS
	.map(load_images, num_parallel_calls=AUTOTUNE)
	.cache()
	.batch(config.BS)
	.prefetch(AUTOTUNE)
)

# initialize our CancerNet model and compile it
model = CancerNet.build(width=48, height=48, depth=3,
	classes=1)
opt = Adagrad(lr=config.INIT_LR,
	decay=config.INIT_LR / config.NUM_EPOCHS)
model.compile(loss="binary_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# initialize an early stopping callback to prevent the model from
# overfitting
es = EarlyStopping(
	monitor="val_loss",
	patience=config.EARLY_STOPPING_PATIENCE,
	restore_best_weights=True)

# fit the model
H = model.fit(
	x=trainDS,
	validation_data=valDS,
	class_weight=classWeight,
	epochs=config.NUM_EPOCHS,
	callbacks=[es],
	verbose=1)

# evaluate the model on test set
(_, acc) = model.evaluate(testDS)
print("[INFO] test accuracy: {:.2f}%...".format(acc * 100))

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