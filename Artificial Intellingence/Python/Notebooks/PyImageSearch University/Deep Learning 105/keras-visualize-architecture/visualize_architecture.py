# USAGE
# python visualize_architecture.py

# The text version of the tutorial is availabel at the following url
# https://www.pyimagesearch.com/2021/05/22/visualizing-network-architectures-using-keras-and-tensorflow/

# This tutorial will show how to visualise network architectures. This is a very good skill to develop and
# has a couple of advantages, it helps when debugging is needed. The second is that if publishing in any form
# will need to be able to show diagrams of what network is being used in a project. The idea is to generate
# a png showing the nework architecture that a project is using. The hard work is done in this file and the 
# plot_model import which will do the graphics for us.

# This will show each layer as the network is passed through and will show inputs and outputs. Using the VGGNet
# in the example instead of LeNet will show a much deeper network

# import the necessary packages
from pyimagesearch.nn.conv import LeNet
from tensorflow.keras.utils import plot_model

# initialize LeNet and then write the network architecture
# visualization grpah to disk
# This model is the same type as MNIST uses
model = LeNet.build(28, 28, 1, 10)

# to_file saves the generated image to disk
plot_model(model, to_file="lenet.png", show_shapes=True)
