
from keras.utils import load_img
import numpy as np

def preprocess_input(input_image_path):
    img = load_img(input_image_path, color_mode="grayscale")
    img = np.array(img)
    return img