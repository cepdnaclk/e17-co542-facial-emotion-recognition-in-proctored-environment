from flask import jsonify
import joblib
import os
import numpy as np
import tensorflow as tf
# import tensorflow_probability as tfp

# from tensorflow.keras.utils import *
# from tensorflow.keras.models import Sequential

def predict_emotion(input):
    # Google Cloud Storage bucket and file details
    bucket_name = 'nn-bucket-g4-new'
    file_name = 'model_public.pkl'
    # local_model_path = 'model.pkl'  # Local path to store the downloaded model
    local_model_path = './model_public.pkl'  # Local path to store the downloaded model

    loaded_model = tf.saved_model.load('saved_model')
    infer = loaded_model.signatures["serving_default"]
    # Initialize Google Cloud Storage client
    # client = storage.Client()

    # Get the bucket
    # bucket = client.get_bucket(bucket_name)

    # # Download the model file from Google Cloud Storage
    # blob = bucket.blob(file_name)
    # blob.download_to_filename(local_model_path)

    # Load the machine learning model
    print(infer)
    # model = joblib.load(local_model_path)

    # Make a prediction (replace this with your actual prediction logic)
    prediction = loaded_model.predict([input])
    return prediction
    # return jsonify({'prediction': prediction.tolist()})
