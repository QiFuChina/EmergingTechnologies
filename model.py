import tensorflow as tf
# These two lines will read in data automatically
from tensorflow.examples.tutorials.mnist import input_data
# Indices the location and give a value————https://www.tensorflow.org/api_docs/python/tf/one_hot
mnist = input_data.read_data_sets("data/", one_hot=True)
# Set the batch size to control the quantity of train images once
batch_size=500
# Calculator sum batch
n_batch=mnist.train.num_example//batch_size

# Set placeholders
# Each image is 28 pixels by 28 pixels, the result to flatten this array into a vector is 28x28=784
x=tf.placeholder(tf.float32,[None,784])
# Each image only be the one of numbers from 0~9, the digit of image is a one-hot vector
y=tf.placeholder(tf.float32,[None,10])