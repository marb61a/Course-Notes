# USAGE
# python reading_from_disk.py --dataset fruits

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2021/06/14/a-gentle-introduction-to-tf-data-with-tensorflow/
# This tutorial is part 1 of a series of 3 and is an introduction to the Tensorflow Data API

# The dataset that is used is a Kaggle Fruits and Vegetables dataset available from 
# https://www.kaggle.com/jorgebailon/fruits-vegetables

# Tensorflow allows data pipeline to be supercharged. In order to use datasets that are too
# large for memory then the ImageDataGenerator class is used. In TF version 2 this has changed
# which is similar to the approach that PyTorch takes. Instead of using the ImageDataGenerator class
# the TF Data API is used, this (tf.data) is approxmately 38 times faster and  allows us to build 
# complex and highly efficient data processing pipelines in reusable blocks of code. Whenever 
# possible you should consider swapping out ImageDataGenerator calls and utilizing tf.data instead,
# your data processing pipelines will be much faster (and therefore, your model will train faster).

# This 2 tutorial will cover 2 different approaches, loading a dataset from memory and loading a 
# dataset from harddisk. The first one will compare tf.data to ImageDataGenerator when working with
# a dataset that fits entirely in memory.

# The tf.data module, prior to TF version 2 Keras and TF users would have to manually define data
# loading functions. Then they would need to make use of Keras’ ImageDataGenerator function for 
# working with image datasets too large to fit into memory. Neither of these approaches is all that
# great.

# The helpers.py file is in the pyimagesearch folder, it has a benchmark function which takes a couple
# of parameters. The first parameter is datasetGen which is a dataset generator and can be either a
# ImageDataGenerator class or the TF data API instance. The number of steps is the number of batches
# that will be used. It also contains a timing mechanism to ensure that we know how long things are 
# taking to run.

# reading_from_memory.py, ImageDataGenerator is imported from TF, the cifar dataset fits in memory so
# will be used in the example. The AUTOTUNE import will check the machine to see how much data can be
# handled, TF will perform a lot of behind the scenes optimisations. Batch Size will be 64 and the number
# of steps will be 5000. ImageDataGenerator has a flow method which allows for reading from disk in batches
# any dataset that is too large to fit into memory. When creating an instance of TF the from_tensor_slices 
# is used, TF functions will be called in something like a pipeline. Underlying the TF API is a caching
# mechanism which will provide important caching for when TF operations are being run. Both the TF data API
# and ImageDataGenerator class are run in the example.

# In this file reading_from_disk.py, the TF data API will be even quick compared to the ImageDataGenerator 
# class. There is more code needed using tf.data than using ImageDataGenerator. TF is being used for image
# resizing and preprocessing rather than OpenCV but the TF methods have been optimised to work quicker in
# this scenario. Again both of the tf.data() and ImageDataGenerator classes will be run.

# import the necessary packages
from pyimagesearch.helpers import benchmark
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.data import AUTOTUNE
from imutils import paths
import tensorflow as tf
import numpy as np
import argparse
import os

def load_images(imagePath):
	# read the image from disk, decode it, resize it, and scale the
	# pixels intensities to the range [0, 1]
	image = tf.io.read_file(imagePath)
	image = tf.image.decode_png(image, channels=3)
	image = tf.image.resize(image, (96, 96)) / 255.0

	# grab the label and encode it
	label = tf.strings.split(imagePath, os.path.sep)[-2]
	oneHot = label == classNames
	encodedLabel = tf.argmax(oneHot)

	# return the image and the integer encoded label
	return (image, encodedLabel)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset")
args = vars(ap.parse_args())

# initialize batch size and number of steps
BS = 64
NUM_STEPS = 1000

# grab the list of images in our dataset directory and grab all
# unique class names
print("[INFO] loading image paths...")
imagePaths = list(paths.list_images(args["dataset"]))
classNames = np.array(sorted(os.listdir(args["dataset"])))

# build the dataset and data input pipeline
print("[INFO] creating a tf.data input pipeline..")
dataset = tf.data.Dataset.from_tensor_slices(imagePaths)
dataset = (dataset
	.shuffle(1024)
	.map(load_images, num_parallel_calls=AUTOTUNE)
	.cache()
	.repeat()
	.batch(BS)
	.prefetch(AUTOTUNE)
)

# create a standard image generator object
print("[INFO] creating a ImageDataGenerator object...")
imageGen = ImageDataGenerator(rescale=1.0/255)
dataGen = imageGen.flow_from_directory(
	args["dataset"],
	target_size=(96, 96),
	batch_size=BS,
	class_mode="categorical",
	color_mode="rgb")

# benchmark the image data generator and display the number of data
# points generated, along with the time taken to perform the
# operation
totalTime = benchmark(dataGen, NUM_STEPS)
print("[INFO] ImageDataGenerator generated {} images in " \
	  " {:.2f} seconds...".format(
	BS * NUM_STEPS, totalTime))

# create a dataset iterator, benchmark the tf.data pipeline, and
# display the number of data points generated, along with the time
# taken
datasetGen = iter(dataset)
totalTime = benchmark(datasetGen, NUM_STEPS)
print("[INFO] tf.data generated {} images in {:.2f} seconds...".format(
	BS * NUM_STEPS, totalTime))
