# USAGE
# python cnn_regression.py --dataset Houses-dataset/Houses\ Dataset/

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2019/01/28/keras-regression-and-cnns/
# The tutorial covers how to train a Convolutional Neural Network (CNN) for regression 
# prediction with Keras, this will be extended to predict house prices from a set of images
# This is part 2 of 3 of a set of tutorials showing how to perform regression on images.
# The previous tutorial should also be read and fully understood prior to beginning here.

# The dataset that was used previously and is available at - https://github.com/emanhamed/Houses-dataset
# A total of 535 houses are included in the dataset with 4 images for each which gives a
# total of 2140 images but only 392 houses and their images will be used in the tutorial

# Performing regression with CNNs and Keras is fairly simple and requires only 3 steps
# Removing the fully-connected softmax classifier layer typically used for classification
# Replacing it with a fully-connected layer with a single node along with a linear activation
# function. Training the model with a continuous value prediction loss function of which there
# are a few available such as Mean Squared Error or Mean Absolute Error. 

# Again the images can be gotten by cloning the github repo mentioned previously, it is also
# important to remember where on the hard disk they are cloned to as it will be an argument
# passed in on the command line.

# The question is how this training of images using the CNN is going to be done. There are 3
# options available, the first is to pass the images one at a time through the CNN and use 
# the price of the house as the target value for each image. The second option is to utilize 
# multiple inputs with Keras and have four independent CNN-like branches that eventually merge 
# into a single output. The 3rd and final choice is to create a montage that combines/tiles 
# all four images into a single image and then pass the montage through the CNN. The first 
# option is not a good choice as the CNN may become confused as the will be multiple images
# with the same target price. The second option is also not a good idea as in this case it
# is fairly wasteful computationally speaking as it will have 4 separate tensors which also
# make training much more difficult. This leaves the 3rd option as the option that makes the
# most sense.

# In the 3rd option all of the 4 images belonging to a house a combined in to 1 image, this is
# done in the following way, bathroom image in the top-left, bedroom image in the top-right
# frontal view in the bottom-right and kitchen in the bottom-left. This tiled image will then
# go through the CNN with house price as the targeted value. There are benefits to using this
# approach as it allows the CNN to learn from all photos of the house rather than trying to pass
# the house photos through the CNN one at a time. It allows the CNN to learn what are called
# discriminative filters from all houses at once without the risk of confusion due to multiple 
# target values being the same.

# The pyimageserach module is fairly similar apart from the load_house_images in datasets.py
# This function is responsible for loading the dataset of images and combining the to create
# collages which can then be run through this file (cnn_regression.py)


# import the necessary packages
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from pyimagesearch import datasets
from pyimagesearch import models
import numpy as np
import argparse
import locale
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", type=str, required=True,
	help="path to input dataset of house images")
args = vars(ap.parse_args())

# construct the path to the input .txt file that contains information
# on each house in the dataset and then load the dataset
print("[INFO] loading house attributes...")
inputPath = os.path.sep.join([args["dataset"], "HousesInfo.txt"])
df = datasets.load_house_attributes(inputPath)

# load the house images and then scale the pixel intensities to the
# range [0, 1]
print("[INFO] loading house images...")
images = datasets.load_house_images(df, args["dataset"])
images = images / 255.0

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
split = train_test_split(df, images, test_size=0.25, random_state=42)
(trainAttrX, testAttrX, trainImagesX, testImagesX) = split

# find the largest house price in the training set and use it to
# scale our house prices to the range [0, 1] (will lead to better
# training and convergence)
maxPrice = trainAttrX["price"].max()
trainY = trainAttrX["price"] / maxPrice
testY = testAttrX["price"] / maxPrice

# create our Convolutional Neural Network and then compile the model
# using mean absolute percentage error as our loss, implying that we
# seek to minimize the absolute percentage difference between our
# price *predictions* and the *actual prices*
model = models.create_cnn(64, 64, 3, regress=True)
opt = Adam(lr=1e-3, decay=1e-3 / 200)
model.compile(loss="mean_absolute_percentage_error", optimizer=opt)

# train the model
print("[INFO] training model...")
model.fit(x=trainImagesX, y=trainY, 
    validation_data=(testImagesX, testY),
    epochs=200, batch_size=8)

# make predictions on the testing data
print("[INFO] predicting house prices...")
preds = model.predict(testImagesX)

# compute the difference between the *predicted* house prices and the
# *actual* house prices, then compute the percentage difference and
# the absolute percentage difference
diff = preds.flatten() - testY
percentDiff = (diff / testY) * 100
absPercentDiff = np.abs(percentDiff)

# compute the mean and standard deviation of the absolute percentage
# difference
mean = np.mean(absPercentDiff)
std = np.std(absPercentDiff)

# finally, show some statistics on our model
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
print("[INFO] avg. house price: {}, std house price: {}".format(
	locale.currency(df["price"].mean(), grouping=True),
	locale.currency(df["price"].std(), grouping=True)))
print("[INFO] mean: {:.2f}%, std: {:.2f}%".format(mean, std))
