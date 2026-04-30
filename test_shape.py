from app.opencv_utils import preprocess_image
import numpy as np
import os

img_path = r"D:\Certificate_detect\Detection\data\certificates\real\real56.jpeg"

img = preprocess_image(img_path)

print("Shape before expand:", img.shape)

img = np.expand_dims(img, axis=0)

print("Shape after expand:", img.shape)