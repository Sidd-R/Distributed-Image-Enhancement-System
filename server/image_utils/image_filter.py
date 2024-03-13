# implement image filter logic
import cv2
import numpy as np
from PIL import Image

class ImageFilter:
    def __init__(self):
        pass

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
