import os
import numpy as np
from tensorflow.keras.models import load_model
from opencv_utils import preprocess_image

# correct model path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "cert_model.h5")

model = load_model(MODEL_PATH)

def predict(img_path):
    img = preprocess_image(img_path)
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0][0]

    return "REAL" if pred < 0.5 else "FAKE"