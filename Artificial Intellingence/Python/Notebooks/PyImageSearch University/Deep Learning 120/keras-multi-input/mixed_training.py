# USAGE
# python mixed_training.py --dataset Houses-dataset/Houses\ Dataset/

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2019/02/04/keras-multiple-inputs-and-mixed-data/
# This is the third and final part of the series and combines the previous two

# In this tutorial, students will learn how to use Keras for multi-input and mixed data.
# We will learn how to define a Keras architecture capable of accepting multiple inputs, 
# including numerical, categorical, and image data. We’ll then train a single end-to-end
# network on this mixed data. The dataset today will include not only numerical and 
# categorical data, but image data as well. This type of problem is called a multi-input
# mixed-data problem. At this time the model needs to be able to be capable of accepting 
# our multiple inputs as well as generating predictions based on these inputs. The tutorial
# will cover how to a Keras model capable of accepting multiple inputs, including numerical, 
# categorical, and image data, all at the same time. We will then train an end-to-end Keras
# model on the mixed data inputs and then evaluate our model using the multi-inputs. One 
# further definition is needed, mixed data refers to the concept of having multiple types 
# of independent data. People will use the term “mixed data” in machine learning literature 
# when working with multiple data modalities. Developing machine learning systems capable of
# handling mixed data can be extremely challenging as each data type may require separate 
# preprocessing steps, including scaling, normalization, and feature engineering. Working 
# with mixed data is still very much an open area of research and is often heavily dependent 
# on the specific task/end goal

# datasets.py in the pyimagesearch module has changes slightly as the text file holding numeric
# data has changed, in this case bathrooms, bedrooms, area, zipcode, price. Zipcodes where there
# are less than 25 houses will be dropped due to the dataset being imbalanced. Other than this
# the datasets.py file is identical to in the previous lesson as a montage of 4 images being 
# combined into 1 to help processing is still being done. Glob is used for handling image file
# paths.

# In the models.py file there are also some changes, in the create_mlp function there are changes
# previously in the first part of the tutorial there would have been a regression layer with a
# single fully connected node responsible for predicting house prices with a linear activation
# function. This has change though as there is a multi input design where the multi layer perceptron
# (MLP) is combined with a CNN. This means that regress will be set to false and output will be
# the 4 nodes with a ReLu activation function. The regress will also be set to false in the create_cnn
# method and again the 4 dense nodes using ReLu will be used, they are the same size so that both the 
# MLP and CNN are equally represented in the outputs when they are concatenated, the vector at this 
# point will have 8 entries (2 dense layers of 4 nodes)

# The final result of using a combined approach is an error of about 27% which is a huge improvement
# on CNN where the error is 56.91 so image data alone was not good, as it turns out in the example
# there is a huge importance on the area location of a house. This level of error is not true of other
# datasets such as health where both categorical data such as gender and continuous data such as blood
# pressure and images such as x-rays can be used in combination for patient benefit.

# import the necessary packages
from pyimagesearch import datasets
from pyimagesearch import models
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import concatenate
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
print("[INFO] processing data...")
split = train_test_split(df, images, test_size=0.25, random_state=42)
(trainAttrX, testAttrX, trainImagesX, testImagesX) = split

# find the largest house price in the training set and use it to
# scale our house prices to the range [0, 1] (will lead to better
# training and convergence)
maxPrice = trainAttrX["price"].max()
trainY = trainAttrX["price"] / maxPrice
testY = testAttrX["price"] / maxPrice

# process the house attributes data by performing min-max scaling
# on continuous features, one-hot encoding on categorical features,
# and then finally concatenating them together
(trainAttrX, testAttrX) = datasets.process_house_attributes(df,
	trainAttrX, testAttrX)

# create the MLP and CNN models
mlp = models.create_mlp(trainAttrX.shape[1], regress=False)
cnn = models.create_cnn(64, 64, 3, regress=False)

# create the input to our final set of layers as the *output* of both
# the MLP and CNN
combinedInput = concatenate([mlp.output, cnn.output])

# our final FC layer head will have two dense layers, the final one
# being our regression head
x = Dense(4, activation="relu")(combinedInput)
x = Dense(1, activation="linear")(x)

# our final model will accept categorical/numerical data on the MLP
# input and images on the CNN input, outputting a single value (the
# predicted price of the house)
model = Model(inputs=[mlp.input, cnn.input], outputs=x)

# compile the model using mean absolute percentage error as our loss,
# implying that we seek to minimize the absolute percentage difference
# between our price *predictions* and the *actual prices*
opt = Adam(lr=1e-3, decay=1e-3 / 200)
model.compile(loss="mean_absolute_percentage_error", optimizer=opt)

# train the model
print("[INFO] training model...")
model.fit(
	x=[trainAttrX, trainImagesX], y=trainY,
	validation_data=([testAttrX, testImagesX], testY),
	epochs=200, batch_size=8)

# make predictions on the testing data
print("[INFO] predicting house prices...")
preds = model.predict([testAttrX, testImagesX])

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
