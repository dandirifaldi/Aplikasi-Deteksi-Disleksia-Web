from flask import Flask, render_template, redirect, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing import image
# from flask_ngrok import run_with_ngrok
import os



app = Flask(__name__)
model = tf.keras.models.load_model('model2.h5')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imageFile=request.files['image']
    img_path="./images/"+imageFile.filename
    imageFile.save(img_path)

    img=load_img(img_path,target_size=(160,160))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    if classes[0]>0.5:
        return render_template('index.html', prediction='Disleksia')
    else :
        return render_template('index.html', prediction='Normal')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
