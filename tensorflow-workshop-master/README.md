# More information can be found in the following

[random-forests/tensorflow-workshop](https://github.com/random-forests/tensorflow-workshop)
[tensorflow/workshops](https://github.com/tensorflow/workshops)


# Welcome

##  Install TensorFlow version 1.3.0

This code requires **TensorFlow version 1.3**. Please choose the installation option that's right for you.

### 1. Install TensorFlow using Docker

This is the easiest option, but the largest download. It's recommended if you have difficulty using a virtual environment. 

* [How-to run the TensorFlow Docker image on your laptop.](setup/install-docker-local.md)

* [How-to run the TensorFlow Docker image on GCP.](setup/install-docker-cloud.md)

### 2. Install TensorFlow using pip in a Virtual Environment

This is recommended if you prefer the smallest download. If you experience difficulty, try the Docker option above.

* [How-to install TensorFlow using pip.](setup/install-pip.md)



# TensorFlow Workshops

Exercises for use at events. 

## How-to run these notebooks

To run these notebooks, you'll need to:
1. Install TensorFlow
2. Install Jupyter
3. Clone this repo
4. Start Jupyter, and open a notebook

Install TensorFlow by following these [instructions](https://www.tensorflow.org/install/). 

Next, open a terminal and install additional dependencies used by these exercises. Note: if you installed TensorFlow using a virtual environment, be sure to activate the environment before running this command.


```sh 

$ pip install -U numpy jupyter matplotlib pandas Pillow

```

Next, clone the workshops repo.

```sh
$ git clone https://github.com/tensorflow/workshops
$ cd workshops
```

Finally, start Jupyter.

```sh

$ jupyter notebook

```

You will see output on your terminal to indicate the server is running. Towards the end of the output, you will see a line similar to this.

```
Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=e9fbab4702ac162eb1f1fc5...
```

Copy this URL, and paste it into your browser. Finally, navigate to the examples folder, and open the first notebook.

### Slides
Here's a link to slides you can use for this workshop: https://goo.gl/bq8HAE Note: these are very basic at the moment. Improving them is on our roadmap.






### Want to report a bug?

Thanks! Can you please file an issue, or even better, a pull request? We'll be doing this workshop a couple times, and future developers will appreciate your help.

- - -
General disclaimer, this is my personal repo and not an official Google product. If you'd like to use this code, say, to build a mission critical component of your giant space laser, you should know there's no warranty, etc.
