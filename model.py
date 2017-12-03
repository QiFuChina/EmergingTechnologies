import tensorflow as tf
import Upload
# These two lines will read in data automatically
from tensorflow.examples.tutorials.mnist import input_data
# Indices the location and give a value————https://www.tensorflow.org/api_docs/python/tf/one_hot
mnist = input_data.read_data_sets("data/", one_hot=True)
# Set the batch size to control the quantity of train images once
batch_size=500
# Calculator sum batch
n_batch=mnist.train.num_examples//batch_size

# Set placeholders
# Each image is 28 pixels by 28 pixels, the result to flatten this array into a vector is 28x28=784
x=tf.placeholder(tf.float32,[None,784])
# Each image only be the one of numbers from 0~9, the digit of image is a one-hot vector
y=tf.placeholder(tf.float32,[None,10])
# Create two variables 
w=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
# Create a model to predict by using softmax function
prediction=tf.nn.softmax(tf.matmul(x,w)+b)

# Use loss function to calculator loss
loss=tf.reduce_mean(tf.square(y-prediction))

# Gradient Descent function to optimizer the loss value for taining
train_step =tf.train.GradientDescentOptimizer(0.2).minimize(loss)

# Initializer
init=tf.global_variables_initializer()

# Function tf.argmax will return the largest value from two values and tf.equal if true then will return 1 as result ————https://www.tensorflow.org/api_docs/python/tf/argmax
correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))
# Function tf.cast will transfer dtype of correct_prediction to float32,tf.reduce_mean computers the average of the tensor————https://www.tensorflow.org/api_docs/python/tf/reduce_mean
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

# Test model
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(20):
        for batch in range(n_batch):
            batch_xs,batch_ys=mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
            #acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
            sess.run(prediction,feed_dict={x: Upload.load_image(new_array)})
        #print("Item"+str(epoch)+",Testing Accuracy"+str(acc))


# def compare():
#     result= tf.arg_max(prediction,1)