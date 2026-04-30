# def signature_score(path):
#     # placeholder for CNN-based signature model
#     return 0.85

import cv2

def signature_score(img_path):
    img = cv2.imread(img_path)

    # fake heuristic (replace with Siamese later)
    blur = cv2.Laplacian(img, cv2.CV_64F).var()

    if blur < 50:
        return 0.3  # suspicious
    return 0.9
