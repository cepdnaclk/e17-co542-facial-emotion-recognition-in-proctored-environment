
from keras.utils import load_img
import numpy as np

def preprocess_input(input_image):
    img = load_img(input_image,color_mode="grayscale")
    img = np.array(img)