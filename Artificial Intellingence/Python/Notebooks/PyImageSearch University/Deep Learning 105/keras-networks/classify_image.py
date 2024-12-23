# USAGE
# python classify_image.py --image images/soccer_ball.jpg --model vgg16

# The text version of the tutorial can be found at the following address
# https://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/
# It is highly recommended to read this tutorial prior to using the video tutorial.

# Any images can be used in the tutorial so they can be downlaoded and adjust the run command
# accordingly with the image name and path.

# Pre-trained networks inside of Keras are capable of recognizing 1,000 different object categories
# this is similar to the objects that we see in our everyday lives. Previously these pre-trained
# image-net models were separate from core Keras, this necessitated using a standalone library
# https://github.com/fchollet/deep-learning-models. We would then need to copy the code into the 
# project that is being worked on. This has change recently as these pre-trained networks have been
# added to the Keras core, they can be found inside the applications sub-module. 

# All of the above means that Keras now ships with 5 Convolutional Neural Networks that have been
# trained on the imagenet dataset. This can be thought of as a shortcut as it gets rid of the need
# to do some training as the network will already be trained. Learning to use pre-trained networks
# is a skill that is needed by Deep Learning practitioners as it helps understanding things like
# transfer learning, feature extraction.

# The 5 CNN's that Keras now has are VGG16, VGG19, ResNet50, Inception V3, Xception, It is important
# to also understand what ImageNet is. ImageNet can be found at the followin url - http://image-net.org/
# ImageNet is formally a project aimed at (manually) labeling and categorizing images into almost 22,000 
# separate categories of objects, this is done with computer vision research in mind. From a practical
# standpoint when talking about ImageNet is is normall referring to  ImageNet Large Scale Visual 
# Recognition Challenge, or ILSVRC for short where the challenge is to is to train a model that can 
# correctly classify an input image into 1,000 separate object categories. The models are trained on 
# around 1.2 million images with additional numbers available for testing and validation. This challenge
# is the benchmark for Computer Vision algorithms and in recent years it is CNN's that have been at the
# top of the leaderboard.

# VGG16 & VGG 19 was first introduced in a 2014 paper which is at the following url https://arxiv.org/abs/1409.1556
# This is a very simple network as it is only 3×3 convolutional layers stacked on top of each other in increasing depth
# Max_pooling then takes care of the volumne size. Two fully-connected layers, each with 4,096 nodes are then 
# followed by a softmax classifier. The 16 and 19 comes from the number of weight layers, this only a few years
# ago was considered as very deep however recent advances has made depths of over 1000 available. In order to 
# make training easier smaller versions of VGG with less weight layers were trained first. These were then
# converged and used as the initialisations of larger networks in a process that is known as pre-training. This
# process is not used as it is extremely tedious, time consuming and inefficient as an entire network needs to
# be trained before it can be used as the initialisation of a deeper network. This has been replaced for the most
# part by MSRA initialisation, a paper is available here - https://arxiv.org/abs/1502.01852. Another drawback from
# using VGG is that it can get large in size in terms of weights (Over 500mb) this is why although still used in
# Deep Learning other techniques are preferred for some tasks.

# A lot of more traditional network achitectures are sequential in nature, this is not the case for ResNet, this uses
# micro-architecture modules which are also known as network-in-network architectures, this term refers to a set of
# building blocks that are used to build the architecture, a collection of these along with standard layers such as
# CONV make up a micro-architecture. It was first discussed in a paper at the followin url - https://arxiv.org/abs/1512.03385
# this paper demonstrates that extremely deep netowrks can be trained using standard SGD by using residual modules.
# Even though ResNet is much deeper than VGG16 and 19 it is much smaller due to the usage of global average pooling 
# rather than fully-connected layers.

# Inception (in this case v3) was introduced in the following 2014 paper - https://arxiv.org/abs/1409.4842. The goal
# of the inception module is to act as a “multi-level feature extractor” by computing 1×1, 3×3, and 5×5 convolutions
# within the same module of the network. The output of these filters are then stacked along the channel dimension prior
# to being fed into the next layer in the network. The original version of this network was called GoogLeNet but is
# known subsequently known as InceptionN where N is the version number. The weights in this network are again smaller
# the previously mentioned networks and average around 96mb.

# XCeption was proposed by the maintainer of the Keras library, it is an extension of the Inception architecture which
# replaces the standard Inception modules with depthwise separable convolutions. This is smaller again in weight size
# with a size of around 91mb.

# There is anothe possible network called SqueezeNet, it can obtain high levels of accuracy by can be very difficult to 
# train.

# import the necessary packages
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications import Xception # TensorFlow ONLY
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications import VGG19
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-model", "--model", type=str, default="vgg16",
	help="name of pre-trained network to use")
args = vars(ap.parse_args())

# define a dictionary that maps model names to their classes
# inside Keras
MODELS = {
	"vgg16": VGG16,
	"vgg19": VGG19,
	"inception": InceptionV3,
	"xception": Xception, # TensorFlow ONLY
	"resnet": ResNet50
}

# esnure a valid model name was supplied via command line argument
if args["model"] not in MODELS.keys():
	raise AssertionError("The --model command line argument should "
		"be a key in the `MODELS` dictionary")

# initialize the input image shape (224x224 pixels) along with
# the pre-processing function (this might need to be changed
# based on which model we use to classify our image)
inputShape = (224, 224)
preprocess = imagenet_utils.preprocess_input

# if we are using the InceptionV3 or Xception networks, then we
# need to set the input shape to (299x299) [rather than (224x224)]
# and use a different image pre-processing function
if args["model"] in ("inception", "xception"):
	inputShape = (299, 299)
	preprocess = preprocess_input

# load our the network weights from disk (NOTE: if this is the
# first time you are running this script for a given network, the
# weights will need to be downloaded first -- depending on which
# network you are using, the weights can be 90-575MB, so be
# patient; the weights will be cached and subsequent runs of this
# script will be *much* faster)
print("[INFO] loading {}...".format(args["model"]))
Network = MODELS[args["model"]]
model = Network(weights="imagenet")

# load the input image using the Keras helper utility while ensuring
# the image is resized to `inputShape`, the required input dimensions
# for the ImageNet pre-trained network
print("[INFO] loading and pre-processing image...")
image = load_img(args["image"], target_size=inputShape)
image = img_to_array(image)

# our input image is now represented as a NumPy array of shape
# (inputShape[0], inputShape[1], 3) however we need to expand the
# dimension by making the shape (1, inputShape[0], inputShape[1], 3)
# so we can pass it through the network
image = np.expand_dims(image, axis=0)

# pre-process the image using the appropriate function based on the
# model that has been loaded (i.e., mean subtraction, scaling, etc.)
image = preprocess(image)

# classify the image
print("[INFO] classifying image with '{}'...".format(args["model"]))
preds = model.predict(image)
P = imagenet_utils.decode_predictions(preds)

# loop over the predictions and display the rank-5 predictions +
# probabilities to our terminal
for (i, (imagenetID, label, prob)) in enumerate(P[0]):
	print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))

# load the image via OpenCV, draw the top prediction on the image,
# and display the image to our screen
orig = cv2.imread(args["image"])
(imagenetID, label, prob) = P[0][0]
cv2.putText(orig, "Label: {}, {:.2f}%".format(label, prob * 100),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
cv2.imshow("Classification", orig)
cv2.waitKey(0)
