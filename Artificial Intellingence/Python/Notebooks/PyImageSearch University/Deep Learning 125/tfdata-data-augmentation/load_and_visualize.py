# USAGE
# python load_and_visualize.py --dataset dataset/animals
# python load_and_visualize.py --dataset dataset/animals --aug 1 --type layers
# python load_and_visualize.py --dataset dataset/animals --aug 1 --type ops

# import the necessary packages
from tensorflow.keras.layers.experimental import preprocessing
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
	image = tf.image.decode_jpeg(image, channels=3)
	image = tf.image.convert_image_dtype(image, dtype=tf.float32)
	image = tf.image.resize(image, (156, 156))

	# parse the class label from the file path
	label = tf.strings.split(imagePath, os.path.sep)[-2]
	
	# return the image and the label
	return (image, label)

def augment_using_layers(images, labels, aug):
	# pass a batch of images through our data augmentation pipeline
	# and return the augmented images
	images = aug(images)

	# return the image and the label
	return (images, labels)

def augment_using_ops(images, labels):
	# randomly flip the images horizontally, randomly flip the images
	# vertically, and rotate the images by 90 degrees in the counter
	# clock-wise direction
	images = tf.image.random_flip_left_right(images)
	images = tf.image.random_flip_up_down(images)
	images = tf.image.rot90(images)

	# return the image and the label
	return (images, labels)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input images dataset")
ap.add_argument("-a", "--augment", type=bool, default=False,
	help="flag indicating whether or not augmentation will be applied")
ap.add_argument("-t", "--type", choices=["layers", "ops"], 
	help="method to be used to perform data augmentation")
args = vars(ap.parse_args())

# set the batch size
BATCH_SIZE = 8

# grabs all image paths
imagePaths = list(paths.list_images(args["dataset"]))

# build our dataset and data input pipeline
print("[INFO] loading the dataset...")
ds = tf.data.Dataset.from_tensor_slices(imagePaths)
ds = (ds
	.shuffle(len(imagePaths), seed=42)
	.map(load_images, num_parallel_calls=AUTOTUNE)
	.cache()
	.batch(BATCH_SIZE)
)

# check if we should apply data augmentation
if args["augment"]:
	# check if we will be using layers to perform data augmentation
	if args["type"] == "layers":
		# initialize our sequential data augmentation pipeline
		aug = tf.keras.Sequential([
			preprocessing.RandomFlip("horizontal_and_vertical"),
			preprocessing.RandomZoom(
				height_factor=(-0.05, -0.15),
				width_factor=(-0.05, -0.15)),
			preprocessing.RandomRotation(0.3)
		])

		# add data augmentation to our data input pipeline
		ds = (ds
			.map(lambda x, y: augment_using_layers(x, y, aug),
				num_parallel_calls=AUTOTUNE)
		)

	# otherwise, we will be using TensorFlow image operations to
	# perform data augmentation
	else:
		# add data augmentation to our data input pipeline
		ds = (ds
			.map(augment_using_ops, num_parallel_calls=AUTOTUNE)
		)

# complete our data input pipeline
ds = (ds
	.prefetch(AUTOTUNE)
)

# grab a batch of data from our dataset
batch = next(iter(ds))

# initialize a figure
print("[INFO] visualizing the first batch of the dataset...")
title = "With data augmentation {}".format(
	"applied ({})".format(args["type"]) if args["augment"] else \
	"not applied")
fig = plt.figure(figsize=(BATCH_SIZE, BATCH_SIZE))
fig.suptitle(title)

# loop over the batch size
for i in range(0, BATCH_SIZE):
	# grab the image and label from the batch
	(image, label) = (batch[0][i], batch[1][i])

	# create a subplot and plot the image and label
	ax = plt.subplot(2, 4, i + 1)
	plt.imshow(image.numpy())
	plt.title(label.numpy().decode("UTF-8"))
	plt.axis("off")

# show the plot
plt.tight_layout()
plt.show()