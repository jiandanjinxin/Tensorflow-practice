""" This code demonstrates reading the test data and writing 
predictions to an output file.

It should be run from the command line, with one argument:

$ python predict_starter.py [test_file]

where test_file is a .npy file with an identical format to those 
produced by extract_cats_dogs.py for training and validation.

(To test this script, you can use one of those).

This script will create an output file in the same directory 
where it's run, called "predictions.txt".

"""

import sys
import numpy as np
import random
import os

CAT_OUTPUT_LABEL = 1
DOG_OUTPUT_LABEL = 0

TEST_FILE = sys.argv[1]

data = np.load(TEST_FILE).item()

# these are images in exactly the same format
# as your train and validation set
images = data["images"]

# the testing data will also contains a unique id
# for each testing image
# because your training / validation doesn't have this
# we will generate some if this doesn't exist
if "ids" in data:
    ids = data["ids"]
else:
    # generate some random ids
    ids = list(range(0,len(images)))

ids = data["ids"]

# This file will be created if it does not exist
# and overwritten if it does
OUT_FILE = "predictions.txt"

# make a prediction on each image
# and write output to disk
out = open(OUT_FILE, "w")
for i, image in enumerate(images):

  image_id = ids[i]

  # here, we'll create a "random" prediction
  # to demonsate the format of the output file
  # this should be "1" for Cat and "0" for dog.
  prediction = random.choice((0, 1))

  line = str(image_id) + " " + str(prediction) + "\n"
  out.write(line)

out.close()
