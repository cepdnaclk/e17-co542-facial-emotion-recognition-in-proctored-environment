import numpy as np
from keras.utils import load_img
from PIL import Image


# def process_image(image_path):
#     features = []
#     img = load_img(image_path, color_mode="grayscale")
#     img = np.array(img)
#     features.append(img)
#     features = np.array(features)
#     features = features.reshape(len(features), 48, 48, 1)
#     return features/255.0


def process_image(image_path):
    # Open the high-resolution image
    img = Image.open(image_path)

    # Resize the image to 48x48 pixels
    img_resized = img.resize((48, 48))

    # Convert the image to grayscale (if needed)
    img_resized = img_resized.convert('L')

    # Normalize pixel values to be in the range [0, 1]
    img_array = np.array(img_resized) / 255.0

    # Reshape the image array if needed (e.g., for a CNN model)
    img_array = img_array.reshape((1, 48, 48, 1))

    return img_array
