# USAGE
# python sgd.py

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2016/10/17/stochastic-gradient-descent-sgd-with-python/

# The previous tutorial dealt with gradient descent but that was a vanilla implementation
# It is slow to run on large datasets and also wastes a lot of computing resources.
# Instead, we should apply Stochastic Gradient Descent (SGD) which is a simple modification 
# to the standard gradient descent algorithm. SGD computes the gradient and updates the 
# weight matrix W on small batches of training data, rather than the entire training set
# which is what the vanilla implementation does. This does have some side effects such as
# more noisy updates and more steps needed along the gradient due to one step per each 
# batch versus one step per epoch. This ultimately leads to faster convergence and no 
# negative effects to loss and classification accuracy

# SGD is arguably the most important algorithm when it comes to training deep neural networks
# and is used extensively in Deep Learning due to it being the engine that enables us to train 
# large networks to learn patterns from data points. It is also recommended to go through the 
# text tutorial prior to the video tutorial and then again after as undestanding SGD is important
# if wanting to become a deep learning practitioner. 

# The reason for the slowness of vanilla Gradient descent is because each iteration of gradient
# descent requires us to compute a prediction for each training point in our training data before 
# being allowed to update the weight matrix. This means using something like ImageNet which has 
# over 1.2 million training images can continue for a very long time. The way around this is to
# do the updates in batches. The only difference between vanilla gradient descent and SGD is the
# addition of a batch training function which computes on a sample of the data which produces a
# batch which can have the gradient evaluated on it. In an ideal scenario batch sizes would be 
# set to 1 but standard batch sizes are 32, 64, 128, and 256. 

# There are reasons for using batch sizes that are greater than 1. Having above 1 in the batch
# size reduces variance in the parameter updates which leads to more stable convergence. The 
# second reason is that powers of two are often desirable for batch sizes as they allow internal
# linear algebra optimization libraries to be more efficient. The mini batch size parameter is not
# a hugely important parameter when hyperparameter tuning.

# import the necessary packages
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import argparse

def sigmoid_activation(x):
	# compute and return the sigmoid activation value for a
	# given input value
	return 1.0 / (1 + np.exp(-x))

def sigmoid_deriv(x):
	# compute the derivative of the sigmoid function ASSUMING
	# that the input "x" has already been passed through the sigmoid
	# activation function
	return x * (1 - x)

def predict(X, W):
	# take the dot product between our features and weight matrix
	preds = sigmoid_activation(X.dot(W))
	# apply a step function to threshold the outputs to binary
	# class labels
	# Clamps values less than 0.5 to 0 and above 0.5 to 1
	preds[preds <= 0.5] = 0
	preds[preds > 0] = 1
	# return the predictions
	return preds

# This is where SGD diverges from vanilla Gradient Descent, the next_batch function takes in 3
# parameters. X is the training dataset of feature vectors/raw image pixel intensities. y is
# the class labels associated with each of the training data points. The third parameter is the 
# size of each mini-batch that will be returned.
def next_batch(X, y, batchSize):
	# loop over our dataset `X` in mini-batches of size `batchSize`
	for i in np.arange(0, X.shape[0], batchSize):
		# yield a tuple of the current batched data and labels
		yield (X[i:i + batchSize], y[i:i + batchSize])

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--epochs", type=float, default=100,
	help="# of epochs")
ap.add_argument("-a", "--alpha", type=float, default=0.01,
	help="learning rate")
# Sets the batch size to 32, again powers of 2 being used is not an accident
# Smaller batch sizes make the loss smaller, a batch size of 1 will have a loss
# significantly smaller than others but takes longer to run
ap.add_argument("-b", "--batch-size", type=int, default=32,
	help="size of SGD mini-batches")
args = vars(ap.parse_args())

# generate a 2-class classification problem with 400 data points,
# where each data point is a 2D feature vector
(X, y) = make_blobs(n_samples=400, n_features=2, centers=2,
	cluster_std=2.5, random_state=95)

# insert a column of 1's as the first entry in the feature
# vector -- this is a little trick that allows us to treat
# the bias as a trainable parameter *within* the weight matrix
# rather than an entirely separate variable
X = np.c_[np.ones((X.shape[0])), X]

# initialize our weight matrix such it has the same number of
# columns as our input features
print("[INFO] starting training...")
W = np.random.uniform(size=(X.shape[1],))

# initialize a list to store the loss value for each epoch
lossHistory = []

# loop over the desired number of epochs
for epoch in np.arange(0, args["epochs"]):
	# initialize the total loss for the epoch
	epochLoss = []

	# loop over our data in batches
	for (batchX, batchY) in next_batch(X, y, args["batch_size"]):
		# take the dot product between our current batch of
		# features and weight matrix `W`, then pass this value
		# through the sigmoid activation function
		preds = sigmoid_activation(batchX.dot(W))

		# now that we have our predictions, we need to determine
		# our `error`, which is the difference between our predictions
		# and the true values
		error = preds - batchY

		# given our `error`, we can compute the total loss value on
		# the batch as the sum of squared loss
		loss = np.sum(error ** 2)
		epochLoss.append(loss)

		# the gradient update is therefore the dot product between
		# the transpose of our current batch and the error on the
		# # batch
		gradient = batchX.T.dot(error) / batchX.shape[0]

		# use the gradient computed on the current batch to take
		# a "step" in the correct direction
		W += -args["alpha"] * gradient

	# update our loss history list by taking the average loss
	# across all batches
	lossHistory.append(np.average(epochLoss))

# compute the line of best fit by setting the sigmoid function
# to 0 and solving for X2 in terms of X1
Y = (-W[0] - (W[1] * X)) / W[2]

# plot the original data along with our line of best fit
plt.figure()
plt.scatter(X[:, 1], X[:, 2], marker="o", c=y)
plt.plot(X, Y, "r-")

# construct a figure that plots the loss over time
fig = plt.figure()
plt.plot(np.arange(0, args["epochs"]), lossHistory)
fig.suptitle("Training Loss")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.show()
