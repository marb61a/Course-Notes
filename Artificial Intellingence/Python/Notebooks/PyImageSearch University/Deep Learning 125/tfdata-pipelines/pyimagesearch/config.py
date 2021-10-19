# import the necessary packages
import os

# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = os.path.join("datasets", "orig")

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = os.path.join("datasets", "idc")

# derive the training, validation, and testing directories
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

# define the amount of data that will be used training
TRAIN_SPLIT = 0.8

# the amount of validation data will be a percentage of the
# *training* data
VAL_SPLIT = 0.1

# define input image spatial dimensions
IMAGE_SIZE = (48, 48)

# initialize our number of epochs, early stopping patience, initial
# learning rate, and batch size
NUM_EPOCHS = 40
EARLY_STOPPING_PATIENCE = 5
INIT_LR = 1e-2
BS = 128