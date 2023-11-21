from flask import Flask, request, render_template
import numpy as np
from predictor import predict_emotion
from helper import allowed_file

from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'

DEFAULT_INPUT = [
    0.19147985,0.51530331,0.5672743,0.07323614,0.03883677,0.23285248
    ,0.02315709,0.62730925,0.9250841,0.20687555,0.42861959,0.24566619
    ,0.42203937,0.07783948,0.15982409,0.99081932,0.52071805,0.55374718
    ,0.1018363,0.18126791
]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return render_template('error.html', error="No file part")

    file = request.files['file']

    # If user does not select file, browser also submits an empty part without filename
    if file.filename == '':
        return render_template('error.html', error="No selected file")

    # Check if the file has an allowed extension
    if file and allowed_file(file.filename):
        # Save the uploaded file to the uploads folder
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Call your prediction function with the file path
        result = predict_emotion(file_path)
        print(result)

        # Pass the result to the template
        return render_template('prediction.html', result=result)

    return render_template('error.html', error="File type not allowed")


if __name__ == '__main__':
    app.run(debug=True)
