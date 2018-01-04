# Cat vs. dog classifier with Estimator

A very simplified introduction to TensorFlow using Estimator API for training a
cat vs. dog classifier from the CIFAR-10 dataset. This version is intentionally
simplified and has a lot of room for improvment, in speed and accuracy.

This tutorial uses Estimator which is an object-oriented high-level API for
training and evaluating models in TensorFlow.

Note: this repo intentionally leaves out the dataset. Download the data from
the link below.

Some useful links:
* CIFAR-10 dataset: http://www.cs.toronto.edu/~kriz/cifar.html
* Install TensorFlow: https://www.tensorflow.org/install/
* TensorFlow Estimator: https://www.tensorflow.org/extend/estimators

For a more in-depth introduction to convolutional neural networks in
TensorFlow without Estimator, please read the official tutorial:
https://www.tensorflow.org/tutorials/deep_cnn

---

Short installation guide (assuming you have virtualenv):
```
virtualenv --system-site-packages ~/tensorflow
source ~/tensorflow/bin/activate
pip install --upgrade tensorflow
pip install --upgrade Pillow
curl -O http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
tar xvf cifar-10-python.tar.gz
```

Run with (python 2.7):
```
python extract_cats_dogs.py
python main.py train
python main.py predict cat.jpg
```

On 2.8GHz Intel Core i7, 25 epochs takes under 10 minutes to train and
should achieve 1.0 train accuracy.

To view the graph, and training metrics, use Tensorboard:
```
tensorboard --logdir=models/
```

