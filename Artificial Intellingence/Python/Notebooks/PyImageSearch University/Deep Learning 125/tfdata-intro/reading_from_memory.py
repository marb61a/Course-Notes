# USAGE
# python reading_from_memory.py

# import the necessary packages
from pyimagesearch.helpers import benchmark
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.datasets import cifar100
from tensorflow.data import AUTOTUNE
import tensorflow as tf

# initialize the batch size and number of steps
BS = 64
NUM_STEPS = 5000

# load the CIFAR-10 dataset from
print("[INFO] loading the cifar100 dataset...")
((trainX, trainY), (testX, testY)) = cifar100.load_data()

# create a standard image generator object
print("[INFO] creating a ImageDataGenerator object...")
imageGen = ImageDataGenerator()
dataGen = imageGen.flow(
	x=trainX, y=trainY,
	batch_size=BS, shuffle=True)

# build a TensorFlow dataset from the training data
dataset = tf.data.Dataset.from_tensor_slices((trainX, trainY))

# build the data input pipeline
print("[INFO] creating a tf.data input pipeline..")
dataset = (dataset
	.shuffle(1024)
	.cache()
	.repeat()
	.batch(BS)
	.prefetch(AUTOTUNE)
)

# benchmark the image data generator and display the number of data
# points generated, along with the time taken to perform the
# operation
totalTime = benchmark(dataGen, NUM_STEPS)
print("[INFO] ImageDataGenerator generated {} images in " \
	  " {:.2f} seconds...".format(
	BS * NUM_STEPS, totalTime))

# create a dataset iterator, benchmark the tf.data pipeline, and
# display the number of data points generator along with the time taken
datasetGen = iter(dataset)
totalTime = benchmark(datasetGen, NUM_STEPS)
print("[INFO] tf.data generated {} images in {:.2f} seconds...".format(
	BS * NUM_STEPS, totalTime))