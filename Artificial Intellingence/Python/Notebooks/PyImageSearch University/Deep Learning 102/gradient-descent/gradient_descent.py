# USAGE
# python gradient_descent.py

# Suggested links 
# https://www.youtube.com/watch?v=ruuW4-InUxM --> Homework on analytical and numerical computation of gradient and Hessian
# https://cs231n.github.io/optimization-1/ --> CS231 Notes

# The text version of the tutorial is available at the following address
# https://www.pyimagesearch.com/2016/10/10/gradient-descent-with-python/

# Gradient Descent is the workhorse behind most Deep Learning, there are
# multiple different types such as Stochastic Gradient Descent. It is vitally 
# important to understand Gradient Descent thoroughly in order to understand
# Neural Networks and Deep Learning, students should also spend time reading
# the text version prior to watching the video training. Explanations of code
# will be given that will not make sense without reading first. 

# As parameterised learning and loss functions have been covered then it is
# necessary to cover what is a key topic in ML\DL namely Optimisation. These
# algorithms are the engines that power neural networks and enable them to learn 
# patterns from data

# Obtaining a high accuracy classifier is dependent on finding a set of weights W and b
# so that data points are correctly classified. The question arises though as to how we
# would go about finding and obtaining a weight matrix W and bias vector b that obtains 
# high classification accuracy. We could try brute force which involves initialising and
# evalutaing over and over again in the hope that a reasonable classification arrives with
# us. As there are DL networks that take millions of parameters this approach could take
# a very long time to pay off. Another approach is to use an algorithm which will allow us
# to improve W and b which is where Gradient Descent comes into play.

# Although Gradient Descent comes in different flavours in each the idea is the same which is
# iteratively evaluate your parameters, compute your loss, then take a small step in the direction 
# that will minimize your loss.

# The gradient descent method is an iterative optimization algorithm that operates over a loss landscape
# this is also known as the optimization surface. The canonical gradient descent example is to visualize
# weights along the x-axis and then the loss for a given set of weights along the y-axis. A loss landscape 
# has many peaks and valleys based on which values the parameters take on. Each peak is a local maximum that 
# represents very high regions of loss, the local maximum with the largest loss across the entire loss
# landscape is the global maximum. There is also the concept of a local minimum which represents small
# regions of loss. Also the local minimum with the smallest loss is the global minimum. Ideally we
# would be able to find this global minimum to ensure that parameters take on the most optimal values.

# The question is the raised as to why we would not jump straight to the global minimum and the answer
# to the question is that the loss landscape is invisible as we do not knwo what it looks like, this
# causes an issue for an optimisation algorithm which is placed blindly on to a plot and has to try and
# navigate to a loss minimum without going to a loss maximum instead.

# The answer to the above problem is to apply gradient descent. In dimensions > 1, our gradient becomes a 
# vector of partial derivatives. There are problems with this in that it is both very slow and is only an
# approximation, in the real wrld it is more likely that analytic descent is used. Using tha idea of a
# bowl means that the loss landscape is treated as a convex problem even though it is not. This also 
# means that a local minimum is also a global minimum in all cases. The issue we then face is that nearly 
# all problems we apply neural networks and deep learning algorithms to are not neat, convex functions. 

# There is a trick called the bias trick available which allows for combining weight matrix W and bias 
# vector b into a single parameter

# import the necessary packages
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import argparse

def sigmoid_activation(x):
	# compute and return the sigmoid activation value for a
	# given input value
	return 1.0 / (1 + np.exp(-x))

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--epochs", type=float, default=100,
	help="# of epochs")
ap.add_argument("-a", "--alpha", type=float, default=0.01,
	help="learning rate")
args = vars(ap.parse_args())

# generate a 2-class classification problem with 250 data points,
# where each data point is a 2D feature vector
(X, y) = make_blobs(n_samples=250, n_features=2, centers=2,
	cluster_std=1.05, random_state=20)

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
	# take the dot product between our features `X` and the
	# weight matrix `W`, then pass this value through the
	# sigmoid activation function, thereby giving us our
	# predictions on the dataset
	preds = sigmoid_activation(X.dot(W))

	# now that we have our predictions, we need to determine
	# our `error`, which is the difference between our predictions
	# and the true values
	error = preds - y

	# given our `error`, we can compute the total loss value as
	# the sum of squared loss -- ideally, our loss should
	# decrease as we continue training
	loss = np.sum(error ** 2)
	lossHistory.append(loss)
	print("[INFO] epoch #{}, loss={:.7f}".format(epoch + 1, loss))

	# the gradient update is therefore the dot product between
	# the transpose of `X` and our error, scaled by the total
	# number of data points in `X`
	gradient = X.T.dot(error) / X.shape[0]

	# in the update stage, all we need to do is nudge our weight
	# matrix in the opposite direction of the gradient (hence the
	# term "gradient descent" by taking a small step towards a
	# set of "more optimal" parameters
	W += -args["alpha"] * gradient

# to demonstrate how to use our weight matrix as a classifier,
# let's look over our a sample of training examples
for i in np.random.choice(250, 10):
	# compute the prediction by taking the dot product of the
	# current feature vector with the weight matrix W, then
	# passing it through the sigmoid activation function
	activation = sigmoid_activation(X[i].dot(W))

	# the sigmoid function is defined over the range y=[0, 1],
	# so we can use 0.5 as our threshold -- if `activation` is
	# below 0.5, it's class `0`; otherwise it's class `1`
	label = 0 if activation < 0.5 else 1

	# show our output classification
	print("activation={:.4f}; predicted_label={}, true_label={}".format(
		activation, label, y[i]))

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
