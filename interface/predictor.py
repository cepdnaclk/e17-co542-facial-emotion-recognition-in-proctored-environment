from flask import jsonify
import joblib
import os
import numpy as np
import tensorflow as tf
from preprocess import preprocess_input
# import tensorflow_probability as tfp

# from tensorflow.keras.utils import *
# from tensorflow.keras.models import Sequential

def predict_emotion(input_file_path):
    # Google Cloud Storage bucket and file details
    local_model_path = './model_public.pkl'  # Local path to store the downloaded model

    loaded_model = tf.saved_model.load('saved_model')
    infer = loaded_model.signatures["serving_default"]

    image = preprocess_input(input_file_path)

    # Load the machine learning model
    print(infer)

    # Make a prediction (replace this with your actual prediction logic)
    prediction = loaded_model.predict([image])
    return prediction
    # return jsonify({'prediction': prediction.tolist()})
