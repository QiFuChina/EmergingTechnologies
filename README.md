# EmergingTechnologies
### Author: Qi Fu
### Modeul: EmergingTechnologies
* Lecturer: Dr [Ian McLoughlin](https://ianmcloughlin.github.io/)
* Purpose： A Lecture project that create a web application in Python to recognise digits in images

Basic tecnhonlogies 
> Python programming language

> Tensorflow knowledge

> Machine learning theory

Project instruction
> Download [MNIST data set](http://yann.lecun.com/exdb/mnist/) package to train and test model
> Flask file to upload image and recognise digits
> HTML file to show the result


### Work Principle
> * Upload.py creates a web application to allow users upload images from local directory to save at designation folder and use function load_image() to read image and resize it 28 x 28 pixel to resave it as black and white colors, then convert it to numpy array format as [1,784] which one row and 784 cloumns.
  * It contains a part of html code to show a html page when application be started.There is a button to select files and another button to upload image, it also needs a display part to receive the test result.

> * Model.py is a model that uses MNIST data to calculate the prediction and it will test the prediction that by useing image numpy array. After obtain the prediction value, it should be return and showed in the web page.

### Detail
Files of Model.py, Resave.py, and Upload.py can run successful separately but there are some problems with Model and Upload files that Model.py has problems with import Upload.py elements

> * The result of test MNIST data
 ![alt text](https://user-images.githubusercontent.com/24989456/33531511-04c1c93c-d886-11e7-8e09-456218515ce1.jpg)
> * The result of test Upload application
 ![alt text](https://user-images.githubusercontent.com/24989456/33531512-04dafd12-d886-11e7-9c2c-10daac94a9dd.jpg)
