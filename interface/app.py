from flask import Flask
from flask import render_template
import pickle
import numpy as np
from predictor import predict_emotion
DEFAULT_INPUT = [
    0.19147985,0.51530331,0.5672743,0.07323614,0.03883677,0.23285248
    ,0.02315709,0.62730925,0.9250841,0.20687555,0.42861959,0.24566619
    ,0.42203937,0.07783948,0.15982409,0.99081932,0.52071805,0.55374718
    ,0.1018363,0.18126791
]
app = Flask(__name__)

@app.route("/")
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/predict')
def predict(input=DEFAULT_INPUT):
    result = predict_emotion(input)
    print(result)
    return render_template('prediction.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
