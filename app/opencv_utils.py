# import cv2
# import numpy as np

# def preprocess_image(img_path):
#     # Read image
#     img = cv2.imread(img_path)

#     # Resize
#     img = cv2.resize(img, (224, 224))

#     # Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Edge detection (important for forgery)
#     edges = cv2.Canny(gray, 50, 150)

#     # Blur detection
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)

#     # Combine features
#     combined = cv2.addWeighted(gray, 0.5, edges, 0.3, 0)
#     combined = cv2.addWeighted(combined, 0.7, blur, 0.3, 0)

#     # Normalize
#     combined = combined / 255.0

#     # Convert to 3-channel (CNN needs it)
#     combined = np.stack((combined,)*3, axis=-1)

#     return combined






import cv2
import numpy as np

def preprocess_image(path):
    img = cv2.imread(path)

    if img is None:
        raise ValueError(f"Image not found or invalid path: {path}")

    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = img / 255.0

    return img