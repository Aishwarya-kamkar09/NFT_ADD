import sys
import os
import numpy as np
from flask import Flask, render_template, request

from utils import get_file_hash

# ==============================
# PATH SETUP
# ==============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==============================
# IMPORT MODULES
# ==============================
from predict import predict
from ocr import extract_text, text_score
from watermark import watermark_score
from signature import signature_score

from blockchain.blockchain import store_hash, verify_hash   
from utils import get_file_hash

# ==============================
# FLASK APP
# ==============================
app = Flask(__name__, template_folder=TEMPLATE_DIR)

# ==============================
# ROUTE
# ==============================
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html", result={"error": "No file selected"})

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        file_hash = get_file_hash(path)

        # ==============================
        # 1. CNN
        # ==============================
        cnn_label = predict(path)
        cnn_score = 1.0 if cnn_label == "REAL" else 0.2

        # ==============================
        # 2. OCR
        # ==============================
        text = extract_text(path)
        ocr_score = text_score(text)

        # ==============================
        # 3. SIGNATURE
        # ==============================
        sig_score = signature_score(path)

        # ==============================
        # 4. WATERMARK
        # ==============================
        wm_score = watermark_score(path)

        # ==============================
        # FINAL SCORE
        # ==============================
        final_score = (
            0.4 * cnn_score +
            0.2 * ocr_score +
            0.2 * sig_score +
            0.2 * wm_score
        )

        label = "REAL" if final_score > 0.75 else "FAKE"

        result = {
            "label": label,
            "confidence": round(final_score, 3),
            "hash": file_hash[:16]
        }

    return render_template("index.html", result=result)



@app.route("/verify", methods=["POST"])
def verify_certificate():
    file = request.files["file"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # STEP 1: generate hash
    file_hash = get_file_hash(path)

    # STEP 2: check blockchain
    is_valid = verify_hash(file_hash)

    if is_valid:
        result = {
            "status": "REAL",
            "message": "Certificate verified on blockchain ✅",
            "hash": file_hash[:20]
        }
    else:
        result = {
            "status": "FAKE",
            "message": "Certificate NOT found on blockchain ❌",
            "hash": file_hash[:20]
        }

    return render_template("verify.html", result=result)

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    app.run(debug=True, port=5001)