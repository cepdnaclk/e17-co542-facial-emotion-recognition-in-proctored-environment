import tensorflow as tf
import config

def load_model(path):
    loaded_model = tf.keras.models.load_model(path)
    return loaded_model

def predict_emotion(image, model=load_model(path=config.MODEL_PATH)):
    prediction = model.predict(image)
    if len(prediction) > 0:
        output = prediction[0]
    else:
        output = [None] * 7

    # Create a dictionary from the lists
    data_dict = dict(zip(config.EMOTION_LABELS, output))
    return data_dict
