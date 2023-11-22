import numpy as np
from keras.utils import load_img

def process_image(image_path):
    features = []
    img = load_img(image_path,color_mode="grayscale")
    img = np.array(img)
    features.append(img)
    features = np.array(features)
    features = features.reshape(len(features),48,48,1)
    return features/255.0

