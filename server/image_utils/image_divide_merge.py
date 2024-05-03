# implement image divide and merge logic using opencv
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, array_to_img
from PIL import Image

# implement image filter logic
import cv2
import numpy as np
from PIL import Image

class ImageFilter:
    def __init__(self):
        pass

    def divide(self, img_rgb, num_rows=4, num_cols=4):
        # implement image divide logic
        img_normalized = img_rgb / 255.0
        img_keras = img_to_array(img_normalized)
        img_keras = np.expand_dims(img_keras, axis=0)
        patch_size = (img_keras.shape[1] // num_cols, img_keras.shape[2] // num_rows)

        patches = tf.image.extract_patches( 
            images=img_keras,
            sizes=[1, *patch_size, 1],
            strides=[1, patch_size[0], patch_size[1], 1],
            rates=[1, 1, 1, 1],
            padding='VALID',
        )
        patches = tf.reshape(patches, (-1, *patch_size, 3))
        pil_patches = []
        for patch in patches:
            pil_patches.append(array_to_img(patch.numpy()))

        return pil_patches

    def merge(patches, num_rows=4, num_cols=4):
        # implement image merge logic
        patch_width, patch_height = patches[0].size

        # Calculate the dimensions of the merged image
        merged_width = patch_width * num_cols
        merged_height = patch_height * num_rows

        # Create a new blank image to merge patches into
        merged_image = Image.new('RGB', (merged_width, merged_height))

        # Merge patches into the blank image
        for i, patch in enumerate(patches):
            row = i // num_cols
            col = i % num_cols
            x_offset = col * patch_width
            y_offset = row * patch_height
            merged_image.paste(patch, (x_offset, y_offset))

        return merged_image
    def filter(self, image, choice):
        # implement image filter logic
        image = np.array(image)
        if choice == 0:
            kernel = np.ones((5, 5), np.uint8) 
            image = cv2.erode(image, kernel, iterations=1)
        elif choice == 1:
            kernel = np.ones((5, 5), np.uint8) 
            image = cv2.dilate(image, kernel, iterations=1)
        elif choice == 2:
            kernel = np.ones((5, 5), np.uint8)
            image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
        elif choice == 3:
            image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15) 
        return Image.fromarray(image)
