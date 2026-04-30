

# import pytesseract
# import cv2
# import os

# pytesseract.pytesseract.tesseract_cmd = r"D:\Certificate_detect\Detection\app\tesseract.exe"

# def extract_text(path):
#     img = cv2.imread(path)
#     if img is None:
#         return ""

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     text = pytesseract.image_to_string(gray)
#     return text.lower()


# def text_score(text):
#     if not text:
#         return 0.0

#     keywords = ["certificate", "degree", "university", "issued", "completion"]

#     hits = sum(k in text for k in keywords)

#     return min(hits / len(keywords), 1.0)





import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"D:\Certificate_detect\Detection\app\tesseract.exe"


def extract_text(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)
    return text.lower()


def text_score(text):
    suspicious_words = ["fake", "copy", "duplicate", "sample"]

    score = 1.0
    for word in suspicious_words:
        if word in text:
            score -= 0.3

    return max(0.0, score)