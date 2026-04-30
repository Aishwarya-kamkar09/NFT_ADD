# import cv2
# import numpy as np

# def watermark_score(path):
#     img = cv2.imread(path, 0)

#     edges = cv2.Canny(img, 50, 150)

#     return np.mean(edges) / 255



import cv2

def watermark_score(img_path):
    img = cv2.imread(img_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect faint patterns
    edges = cv2.Canny(gray, 100, 200)

    ratio = edges.mean() / 255

    if ratio < 0.05:
        return 0.4  # no watermark
    return 0.9