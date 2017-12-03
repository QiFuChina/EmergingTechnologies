import os
from PIL import Image as pil
# Import python image library to handle images
import numpy as np
# Import numpy library to convert the image to array

# Define a global variable
#@app.route('/uploads')
def load_image():
    im=pil.open("uploads/123.jpg").convert("L")
    # Open one image from folder and convert it to black and white image
    im=im.resize((28,28))
    # Resize the image
    #im.show()
    new_im=im.save("uploads/456.jpg")
    # Save it as a new image with other name
    #im=np.array(im,'f')
    new_im=np.array(im,'f')
    # Convert image to numpy array format
    
    #im=np.reshape[28,28]
    #im=np.reshape(im,(28,28))
   

    rows,cols=new_im.shape
    for i in range(rows):
        for j in range(cols):
            if(new_im[i,j]<=128):
                new_im[i,j]=0
            else:
                new_im[i,j]=1
    new_array=np.reshape(new_im,(1,784))
    # Set a new arrar to reshape the original array as one row and 784 cloumns 
    #im=pil.fromarray(im)

    #im.save("6.jpg")
    print(new_array)
    
   # data=im.getdata()
    #data=np.matrix(data)

    #data=np.reshape(data,(28,28))
    #new_im=pil.fromarray(data)
    #print(np.asarray(im))
    #new_im.save("aa.jpg")

if __name__=="__main__":
    load_image()

