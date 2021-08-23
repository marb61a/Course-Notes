# The text version of the tutorial is available at the following url
# https://www.pyimagesearch.com/2021/05/06/implementing-the-perceptron-neural-network-with-python/

# Rosenblatt in 1958, The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain 
# https://doi.org/10.1037/h0042519

# The purpose of the tutorial is to implement the perceptron neural network architecture using python
# It is going to be a pure Python implementation rather than using libraries. This is the equivalent
# of hello world when doing AI related programming. The reason that the perceptron implementation is
# considered as a hello world style program is that it is very easy.

# There are 3 scripts in the root folder of the lesson, these will reflect the bitwise operations available
# It should be remembered that XOR is not linearly seperable, there is no line that can be drawn to separate
# 2 classes, the XOR issue had huge effects on AI research in the 1960s as it was misunderstood that all 
# forms of XOR could not be separated.

# The pyimagesearch module will be built upon as the module evolves
# Understand bitwise datasets --> https://www.geeksforgeeks.org/python-bitwise-operators/

# The XOR script will not return the correct result no matter how often the script is ran, there will usually be
# 50% wrong. It is this issue that led to the 'AI Winter'. There may be occasions where AND and OR files also
# return wrong answers, this is due to weights. Students should experiment with the various parameters when it
# does to see what adjustments returns a correct answer


# import the necessary packages
import numpy as np

class Perceptron:
	# Constructor, N is the number of features
	def __init__(self, N, alpha=0.1):
		# initialize the weight matrix and store the learning rate
		self.W = np.random.randn(N + 1) / np.sqrt(N)
		self.alpha = alpha

	def step(self, x):
		# apply the step function
		return 1 if x > 0 else 0

	# Trains the perceptron, y is the target predicted outcome
	def fit(self, X, y, epochs=10):
		# insert a column of 1's as the last entry in the feature
		# matrix -- this little trick allows us to treat the bias
		# as a trainable parameter within the weight matrix
		X = np.c_[X, np.ones((X.shape[0]))]

		# loop over the desired number of epochs sequentially, this is the
		# standard training procedure for the perceptron
		for epoch in np.arange(0, epochs):
			# loop over each individual data point
			for (x, target) in zip(X, y):
				# take the dot product between the input features
				# and the weight matrix, then pass this value
				# through the step function to obtain the prediction
				p = self.step(np.dot(x, self.W))

				# only perform a weight update if our prediction
				# does not match the target
				if p != target:
					# determine the error
					error = p - target

					# update the weight matrix
					self.W += -self.alpha * error * x

	def predict(self, X, addBias=True):
		# ensure our input is a matrix
		X = np.atleast_2d(X)

		# check to see if the bias column should be added
		if addBias:
			# insert a column of 1's as the last entry in the feature
			# matrix (bias)
			X = np.c_[X, np.ones((X.shape[0]))]

		# take the dot product between the input features and the
		# weight matrix, then pass the value through the step
		# function
		return self.step(np.dot(X, self.W))
