import os

from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory

from PIL import Image as pil
# Import python image library to handle images
import numpy as np
# Import numpy library to convert the image to array

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

#@app.route()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename("123.jpg")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',filename=filename))
            #return img('uploaded_file',filename=filename)
        load_image()
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
        <div class="display_window">
         <img>
    </form>
    '''
    # def load_image():
    #         im=pil.open("uploads/123.jpg").convert("L")
    #         im=im.resize((28,28))
    #         new_im=im.save("uploads/456.jpg")
    #         new_im=np.array(im,'f')
    #         rows,cols=new_im.shape
    #         for i in range(rows):
    #             for j in range(cols):
    #                 if(new_im[i,j]<=128):
    #                     new_im[i,j]=0
    #                 else:
    #                     new_im[i,j]=1
    #         new_im=np.reshape(new_im,(1,784))
    #         print(new_im)
    #         load_image()


# @app.route('/')
def load_image():
    im=pil.open("uploads/123.jpg").convert("L")
    im=im.resize((28,28))
    #im.show()
    new_im=im.save("uploads/456.jpg")
    #im=np.array(im,'f')
    new_im=np.array(im,'f')
    
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
    #im=pil.fromarray(im)

    #im.save("6.jpg")
    print(new_array)
    #load_image()
    #data=im.getdata()
    #data=np.matrix(data)
    #return load_image()
    #data=np.reshape(data,(28,28))
    #new_im=pil.fromarray(data)
    #print(np.asarray(im))
    #new_im.save("aa.jpg")
if __name__=="__main__":
    app.run()